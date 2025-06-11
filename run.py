from app import create_app
from app.config import load_app_config

app = create_app()
config = load_app_config()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=config["flask"].get("port", 8080),
        debug=config["flask"].get("debug", False)
    )
