from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        else:
            protocol_name = "Other"
        
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol_name}")

        if protocol ==6 or protocol == 17:
            payload = packet[IP].payload
            print(f"Payload: {bytes(payload)}")


print("Starting packet capture...")
sniff(prn=packet_callback, store=0)