import yaml
import os
from .db_utils import construct_db_uri

def load_app_config():
    with open("config.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    db_config_path = cfg["database_config_path"]

    if not os.path.isfile(db_config_path):
        raise FileNotFoundError(f"Database config file not found: {db_config_path}")

    with open(db_config_path, "r") as f:
        db_cfg = yaml.safe_load(f)

    db_uri = construct_db_uri(db_cfg)
    return {
        "SQLALCHEMY_DATABASE_URI": db_uri,
        "style": cfg.get("style", {}),
        "flask": cfg.get("flask", {"port": 8080, "debug": False})
    }
