from flask import jsonify, request
from flask import Blueprint

agents = {}
tasks = []
wiki = {}
messages = []


def register_routes(app):
    @app.route('/')
    def index():
        return jsonify({
            'agents': list(agents.values()),
            'tasks': tasks,
            'wiki': wiki,
            'messages': messages
        })

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        agent_id = data.get('id')
        if agent_id:
            agents[agent_id] = {'id': agent_id, 'role': data.get('role', 'agent')}
            return jsonify({'status': 'registered', 'agent': agents[agent_id]})
        return jsonify({'error': 'missing id'}), 400

    @app.route('/task', methods=['POST'])
    def create_task():
        data = request.get_json()
        tasks.append(data)
        return jsonify({'status': 'task added', 'task': data})

    @app.route('/wiki', methods=['POST'])
    def add_wiki():
        data = request.get_json()
        key = data.get('key')
        if key:
            wiki[key] = data.get('content', '')
            return jsonify({'status': 'wiki updated', 'entry': {key: wiki[key]}})
        return jsonify({'error': 'missing key'}), 400

    @app.route('/message', methods=['POST'])
    def send_message():
        data = request.get_json()
        messages.append(data)
        return jsonify({'status': 'message sent', 'message': data})

    @app.route('/inbox/<agent_id>', methods=['GET'])
    def inbox(agent_id):
        inbox_msgs = [msg for msg in messages if msg.get('to') == agent_id]
        return jsonify({'inbox': inbox_msgs})
