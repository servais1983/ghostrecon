#!/bin/bash
echo "[*] Installation de GhostRecon sur Kali Linux..."

sudo apt update
sudo apt install -y python3 python3-pip python3-impacket python3-scapy

pip3 install -r requirements.txt

chmod +x ghostrecon.py

echo "[+] Installation terminée. Utilisez : python3 ghostrecon.py [commande]"
