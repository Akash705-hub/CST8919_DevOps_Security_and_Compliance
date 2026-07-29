import importlib.util
import logging
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
APP_PATH = ROOT / "app.py"


@pytest.fixture(scope="module")
def app_module():
    spec = importlib.util.spec_from_file_location("assignment1_app", APP_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_protected_route_logs_unauthorized_attempt(app_module, monkeypatch, caplog):
    async def fake_get_user(options):
        return None

    monkeypatch.setattr(app_module.auth0, "get_user", fake_get_user)

    with caplog.at_level(logging.WARNING, logger=app_module.app.logger.name):
        with app_module.app.test_client() as client:
            response = client.get("/protected")

    assert response.status_code == 302
    assert any("unauthorized_attempt" in record.getMessage() for record in caplog.records)
