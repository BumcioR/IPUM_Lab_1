# for main.py
import os
import yaml


def load_secrets(path="secrets.yaml") -> None:
    """Wczytuje odszyfrowany plik YAML jako zmienne środowiskowe"""
    if not os.path.exists(path):
        print(f"Secrets file {path} does not exist.")
        return

    with open(path, "r") as f:
        secrets = yaml.safe_load(f)

    for key, value in secrets.items():
        os.environ[key] = str(value)
