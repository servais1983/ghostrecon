from impacket.smbconnection import SMBConnection

def run():
    target = input("Adresse IP cible SMB: ")
    try:
        print(f"[*] Test de session SMB anonyme sur {target}...")
        conn = SMBConnection(target, target)
        conn.login("", "")
        shares = conn.listShares()
        print("[+] Accès SMB ANONYME POSSIBLE !")
        print("Partages disponibles :")
        for share in shares:
            print(f" - {share['shi1_netname'].decode().strip()}")
        conn.close()
    except Exception as e:
        print("[-] Accès SMB anonyme impossible.")
        print(str(e))
