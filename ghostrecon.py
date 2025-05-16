#!/usr/bin/env python3

import argparse
from core import recon, smb_tools, lateral
from core.utils import run_script_yaml

def main():
    parser = argparse.ArgumentParser(prog="ghostrecon", description="CLI Pentest Interne (Kali Linux)")
    subparsers = parser.add_subparsers(dest="command")

    # Reconnaissance
    subparsers.add_parser("recon", help="Scan ARP du réseau local")

    # SMB
    subparsers.add_parser("smb", help="Test de session SMB anonyme")

    # Mouvement latéral
    lateral_parser = subparsers.add_parser("lateral", help="Mouvement latéral")
    lateral_parser.add_argument("--user", required=True)

    # Pentest-as-Code
    script_parser = subparsers.add_parser("run", help="Exécute un scénario YAML")
    script_parser.add_argument("script", help="Fichier YAML de scénario")

    args = parser.parse_args()

    if args.command == "recon":
        recon.run()
    elif args.command == "smb":
        smb_tools.run()
    elif args.command == "lateral":
        lateral.run(args.user)
    elif args.command == "run":
        run_script_yaml(args.script)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
