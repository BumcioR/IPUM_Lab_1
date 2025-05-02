# for main.py
import os
import yaml


def load_secrets(path="secrets.yaml") -> None:
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist. Did you decrypt it?")

    with open(path, "r") as f:
        secrets = yaml.safe_load(f)

    for key, value in secrets.items():
        os.environ[key] = str(value)
