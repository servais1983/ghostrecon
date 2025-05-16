# 🛠️ GhostRecon

## Présentation

**GhostRecon** est un outil de pentest interne pour les professionnels de la sécurité. Il est conçu pour fonctionner **en ligne de commande sur Kali Linux**, avec une architecture modulaire, simple et extensible.

## ✅ Objectifs

* Reconnaissance passive et active du réseau local
* Analyse de services SMB (session anonyme, partages)
* Simulation de mouvements latéraux
* Utilisation de **scénarios YAML** (pentest-as-code)
* Compatible **nativement avec Kali Linux**

## 📦 Installation

```bash
git clone https://github.com/servais1983/ghostrecon.git
cd ghostrecon
chmod +x install.sh
./install.sh
```

## ⚙️ Exemples d'utilisation

```bash
sudo python3 ghostrecon.py recon
python3 ghostrecon.py smb
python3 ghostrecon.py lateral --user admin
python3 ghostrecon.py run scripts/lateral_move.yaml
```

> ⚠️ **Note** : Les fonctions comme `recon` nécessitent les **droits root** sur Kali Linux.

## 🔍 Fonctionnalités

### Reconnaissance réseau
Détecte automatiquement les hôtes actifs sur le réseau local à l'aide de scans ARP.

### Tests SMB
Teste les connexions SMB anonymes et liste les partages accessibles.

### Simulation de mouvements latéraux
Simule des tentatives de mouvements latéraux pour tester la sécurité du réseau interne.

### Pentest-as-Code
Utilise des fichiers YAML pour définir des scénarios de tests automatisés.

## 📋 Prérequis

- Kali Linux (recommandé)
- Python 3.7+
- Privilèges sudo/root pour certaines fonctionnalités

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🧩 Extensions futures

* Intégration LDAP / AD via `ldap3`
* Détection de vulnérabilités sur les ports ouverts
* Intégration avec BloodHound ou CrackMapExec
* Mode "stealth" : scans lents, randomisés
* IA locale pour suggérer des attaques (via LLM)
