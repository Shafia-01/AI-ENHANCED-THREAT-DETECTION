import statistics

def extract_features(packets):
    if not packets:
        return None

    flow_durations = []
    packet_lengths = []
    flow_iat = []
    fwd_iat = []
    bwd_iat = []

    fwd_packet_lengths = []
    bwd_packet_lengths = []
    fwd_packet_count = 0
    bwd_packet_count = 0
    fwd_total_length = 0
    bwd_total_length = 0
    destination_port = 0

    for i in range(1, len(packets)):
        pkt = packets[i]
        flow_durations.append(pkt.time - packets[0].time)
        flow_iat.append(pkt.time - packets[i - 1].time)

        if hasattr(pkt, "direction") and pkt.direction == "FWD":
            fwd_iat.append(pkt.time - packets[i - 1].time)
            fwd_packet_lengths.append(len(pkt.payload))
            fwd_packet_count += 1
            fwd_total_length += len(pkt.payload)
        else:
            bwd_iat.append(pkt.time - packets[i - 1].time)
            bwd_packet_lengths.append(len(pkt.payload))
            bwd_packet_count += 1
            bwd_total_length += len(pkt.payload)

        packet_lengths.append(len(pkt.payload))

        if hasattr(pkt, "dport"):
            destination_port = pkt.dport

    if not packet_lengths:
        packet_lengths = [0]

    feature_dict = {
        'Flow Duration': sum(flow_durations) / len(flow_durations) if flow_durations else 0,
        'Bwd Packet Length Max': max(bwd_packet_lengths) if bwd_packet_lengths else 0,
        'Bwd Packet Length Min': min(bwd_packet_lengths) if bwd_packet_lengths else 0,
        'Bwd Packet Length Mean': statistics.mean(bwd_packet_lengths) if bwd_packet_lengths else 0,
        'Bwd Packet Length Std': statistics.stdev(bwd_packet_lengths) if len(bwd_packet_lengths) > 1 else 0,
        'Flow IAT Mean': statistics.mean(flow_iat) if flow_iat else 0,
        'Flow IAT Std': statistics.stdev(flow_iat) if len(flow_iat) > 1 else 0,
        'Flow IAT Max': max(flow_iat) if flow_iat else 0,
        'Fwd IAT Total': sum(fwd_iat) if fwd_iat else 0,
        'Fwd IAT Std': statistics.stdev(fwd_iat) if len(fwd_iat) > 1 else 0,
        'Fwd IAT Max': max(fwd_iat) if fwd_iat else 0,
        'Max Packet Length': max(packet_lengths),
        'Packet Length Mean': statistics.mean(packet_lengths),
        'Packet Length Std': statistics.stdev(packet_lengths) if len(packet_lengths) > 1 else 0,
        'Packet Length Variance': statistics.variance(packet_lengths) if len(packet_lengths) > 1 else 0,
        'Average Packet Size': statistics.mean(packet_lengths),
        'Avg Bwd Segment Size': statistics.mean(bwd_packet_lengths) if bwd_packet_lengths else 0,
        'Idle Mean': 50,
        'Idle Max': 80,
        'Idle Min': 10,
        'Destination Port': destination_port,
        'Total Fwd Packets': fwd_packet_count,
        'Total Backward Packets': bwd_packet_count,
        'Total Length of Fwd Packets': fwd_total_length,
        'Total Length of Bwd Packets': bwd_total_length,
        'Fwd Packet Length Max': max(fwd_packet_lengths) if fwd_packet_lengths else 0,
        'Fwd Packet Length Min': min(fwd_packet_lengths) if fwd_packet_lengths else 0
    }

    return feature_dict
