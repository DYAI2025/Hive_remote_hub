from flask import Flask
from agenthub.routes import register_routes
import yaml
import os


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    return {}


def create_app():
    app = Flask(__name__)
    config = load_config()
    app.config.update(config)
    register_routes(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
