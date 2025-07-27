from flask import Flask, jsonify, request
import yaml
import os

app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify({"status": "Agent-Hub läuft", "mode": "klar"})

@app.route('/agents')
def list_agents():
    with open("registry.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return jsonify(data.get("agents", []))

@app.route('/wiki/<project>')
def wiki(project):
    path = f"knowledge/{project}.md"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "Nicht gefunden", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7880)
