# agent_hub: Zentrale für GPT-Agents & Projektwissen

# Projektstruktur
# agent_hub/
# ├── app.py                 # Flask-Server, REST-API für GPT-Kommunikation
# ├── registry.yaml           # Liste aller bekannten Projekte & GPT-Agenten
# ├── knowledge/
# │   ├── hive-caller.md     # Markdown-Wissen zu jedem Projekt
# │   └── ...
# ├── logs/
# ├── config.yaml            # Systemweite Einstellungen
# └── README.md

# app.py
from flask import Flask, request, jsonify
import yaml
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_project():
    data = request.json
    with open('registry.yaml', 'r') as f:
        registry = yaml.safe_load(f)
    registry['projects'].append(data)
    with open('registry.yaml', 'w') as f:
        yaml.dump(registry, f)
    return {'status': 'registered'}

@app.route('/wiki/<project>', methods=['GET'])
def get_knowledge(project):
    try:
        with open(f'knowledge/{project}.md', 'r') as f:
            return {'markdown': f.read()}
    except:
        return {'error': 'Not found'}, 404

@app.route('/agents', methods=['GET'])
def list_agents():
    with open('registry.yaml', 'r') as f:
        registry = yaml.safe_load(f)
    return {'agents': registry.get('agents', [])}

if __name__ == '__main__':
    app.run(port=7880)


# registry.yaml
projects:
  - name: hive-caller
    description: Voice-zu-GPT Interface mit Whisper und ElevenLabs
    entrypoint: /apps/hive-caller
    status: active
agents:
  - name: The Hive
    role: Beobachter & Resonanz-Coordinator
    endpoint: internal

# config.yaml
port: 7880
logging: true
storage_path: ./logs
voice_profiles:
  hive: elevenlabs-ben.json
  narion: elevenlabs-narion.json
  dante: elevenlabs-dante.json

# README.md
# Agent-Hub

Eine kleine, autonome Steuerzentrale für GPT-gestützte Agentenprojekte.

## Funktionen
- Projekte registrieren
- Wissen verwalten (Markdown)
- REST-API zur Agentenabfrage

## Start
```bash
pip install flask pyyaml
python app.py
```

## API-Endpunkte
- POST /register
- GET /wiki/<projekt>
- GET /agents
