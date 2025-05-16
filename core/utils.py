import yaml
from core import smb_tools, lateral

def run_script_yaml(path):
    print(f"[*] Chargement du scénario : {path}")
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    for step in data.get("steps", []):
        step_type = step.get("type")
        if step_type == "smb":
            smb_tools.run()
        elif step_type == "lateral_move":
            user = step.get("user", "admin")
            lateral.run(user)
        else:
            print(f"[!] Étape inconnue : {step_type}")
