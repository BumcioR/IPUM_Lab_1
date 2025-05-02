import os
import sys
import pytest

# Ścieżka do katalogu głównego projektu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from settings import Settings
from load_secrets import load_secrets
from dotenv import load_dotenv


@pytest.fixture(autouse=True)
def load_test_env():
    load_dotenv(dotenv_path="config/.env.test", override=True)
    load_secrets()
    yield
    # czyszczenie zmiennych środowiskowych po testach
    for var in ["APP_NAME", "ENVIRONMENT", "API_KEY"]:
        os.environ.pop(var, None)


def test_settings_loaded():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "My Test App"
    assert settings.API_KEY == "my-secret-api-key"
