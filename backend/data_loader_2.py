from scapy.all import sniff
import pandas as pd
from feature_extraction import extract_features

print("⏳ Capturing packets... (this may take a few seconds)")
packets = sniff(count=100, timeout=10)
print(f"✅ Captured {len(packets)} packets.")

features = extract_features(packets)

df = pd.DataFrame([features])
df.to_csv("models/sample_dataset3.csv", index=False)

print("📄 Saved extracted features to models/sample_dataset3.csv")
