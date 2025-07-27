# hive_caller: Projektstruktur mit Python-Integration

# Verzeichnisstruktur (Skizze)
# hive_caller/
# ├── main.py              # Python-Server zur Trigger-Verwaltung
# ├── whisper_listener.py  # Lauscht auf neue Whisper-Dateien / Streams
# ├── electron-ui/         # Electron App mit UI
# │   ├── main.js          # Electron Mainprozess
# │   ├── renderer.js      # UI-Logik
# │   └── index.html       # Einfaches Interface (Start/Stopp)
# ├── connector/           # GPT-Kommunikation
# │   └── responder.py     # Antwortlogik (Text zu Speech)
# ├── assets/              # Icons, Styles
# ├── config.yaml          # Lokale Konfiguration (Hotkey, Pfade)
# └── requirements.txt     # Python-Abhängigkeiten

# main.py
from flask import Flask, request
import subprocess
import threading
import yaml

app = Flask(__name__)

status = {"state": "idle"}

@app.route('/trigger', methods=['POST'])
def trigger():
    status["state"] = "listening"
    subprocess.Popen(["python3", "whisper_listener.py"])
    return {"status": "started"}

@app.route('/status', methods=['GET'])
def get_status():
    return status

if __name__ == '__main__':
    app.run(port=8723)

# connector/responder.py (Ausschnitt)
def generate_response(text):
    # OpenAI oder Claude-API ansprechen, Antwort holen
    # Text-to-Speech mit ElevenLabs, Piper oder TTS-System
    return audio_file_path

# whisper_listener.py (Ausschnitt)
# Lauscht auf neue Dateien von SuperWhisper (oder Mikrofon)
# Sobald erkannt: Transkribieren, an responder senden
