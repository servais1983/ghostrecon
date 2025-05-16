from scapy.all import ARP, Ether, srp

def run():
    print("[*] Scan ARP en cours sur 192.168.1.0/24...")
    target_ip = "192.168.1.0/24"
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    print("[+] Hôtes détectés :")
    for sent, received in result:
        print(f"{received.psrc} - {received.hwsrc}")
