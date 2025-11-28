from scapy.all import *
import time

networks = {}

def callback(packet):
    # Check for beacon frames (type=0, subtype=8)
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode(errors="ignore")
        bssid = packet[Dot11].addr2
        channel = int(ord(packet[Dot11Elt:3].info))
        if bssid not in networks:
            networks[bssid] = (ssid, channel)
            print(f"[+] SSID: {ssid} | BSSID: {bssid} | Channel: {channel}")

def scan(interface):
    print(f"\n[*] Scanning WiFi networks on {interface}...\n")
    sniff(iface=interface, prn=callback, timeout=20)

if __name__ == "__main__":
    interface = input("Enter WiFi interface in monitor mode (e.g., wlan0mon): ")
    scan(interface)

