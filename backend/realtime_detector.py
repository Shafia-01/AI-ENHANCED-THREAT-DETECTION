import time
import joblib
import pandas as pd
import subprocess
import re
from scapy.all import sniff
from backend.feature_extraction import extract_features

model = joblib.load("../models/threat_detection_model.pkl")
scaler = joblib.load("../models/scaler.pkl")
imputer = joblib.load("../models/imputer.pkl")

def get_wifi_info():
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
        ssid = re.search(r"^\s*SSID\s*:\s(.+)$", output, re.MULTILINE)
        protocol = re.search(r"^\s*Radio type\s*:\s(.+)$", output, re.MULTILINE)
        description = re.search(r"^\s*Description\s*:\s(.+)$", output, re.MULTILINE)
        network_band = re.search(r"^\s*Channel\s*:\s(\d+)", output, re.MULTILINE)

        return {
            "SSID": ssid.group(1) if ssid else "N/A",
            "Protocol": protocol.group(1) if protocol else "N/A",
            "Description": description.group(1) if description else "N/A",
            "Network Band (Channel)": f"{network_band.group(1)}" if network_band else "N/A"
        }
    except Exception as e:
        print(f"❌ Error getting Wi-Fi info: {e}")
        return None

def auto_select_interface():
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
        name_match = re.search(r"^\s*Name\s*:\s(.+)$", output, re.MULTILINE)
        return name_match.group(1).strip() if name_match else None
    except Exception as e:
        print(f"❌ Could not auto-select interface: {e}")
        return None

def process_packets(packets):
    features = extract_features(packets)
    if features is None:
        return "⚠️ No packets to process."

    df = pd.DataFrame([features])

    try:
        df_imputed = imputer.transform(df)
        df_scaled = scaler.transform(df_imputed)
        prediction = model.predict(df_scaled)
        return "🚨 Threat Detected!" if prediction[0] == 1 else "✅ Normal Activity"
    except Exception as e:
        print(f"❌ Error in processing pipeline: {e}")
        return "⚠️ Detection Failed"

def sniff_packets_and_detect(timeout=20):
    wifi_info = get_wifi_info()
    iface = auto_select_interface()
    if iface is None:
        return "❌ No Wi-Fi interface detected.", None

    packet_list = []

    def custom_packet_handler(packet):
        packet_list.append(packet)

    sniff(iface=iface, prn=custom_packet_handler, timeout=timeout)

    result = process_packets(packet_list)
    summary = {
        "Packets Captured": len(packet_list),
        "Interface": iface,
        "Wi-Fi Info": wifi_info
    }

    return result, summary

if __name__ == "__main__":
    status, info = sniff_packets_and_detect()
    print("\n🔍 Detection Summary:")
    print(info)
    print(status)
