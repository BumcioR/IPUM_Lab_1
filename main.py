import os
import argparse
from dotenv import load_dotenv
from settings import Settings
from load_secrets import load_secrets  # <- to czyta secrets.yaml do os.environ


def export_envs(environment: str = "dev") -> None:
    env_files = {
        "dev": "config/.env.dev",
        "test": "config/.env.test",
        "prod": "config/.env.prod",
    }
    env_path = env_files.get(environment)
    if not env_path:
        raise ValueError(f"Unsupported environment: {environment}")

    if not os.path.exists(env_path):
        raise FileNotFoundError(f"{env_path} does not exist.")

    print(f"Loading environment file: {env_path}")
    load_dotenv(dotenv_path=env_path, override=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified .env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    load_secrets()  # <- załadowanie secrets.yaml po odszyfrowaniu

    settings = Settings()
    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
