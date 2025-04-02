from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Configure CORS to allow requests from your React frontend
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type"]
    }
})

# In-memory storage for notes
notes = []
note_id_counter = 1

@app.route('/api/notes', methods=['POST'])
def add_note():
    global note_id_counter
    data = request.get_json()
    
    if not data or 'content' not in data:
        return jsonify({"error": "Content is required"}), 400
    
    new_note = {
        "id": note_id_counter,
        "content": data['content']
    }
    notes.append(new_note)
    note_id_counter += 1
    
    return jsonify(new_note), 201

@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    for index, note in enumerate(notes):
        if note['id'] == note_id:
            deleted_note = notes.pop(index)
            return jsonify(deleted_note)
    
    return jsonify({"error": "Note not found"}), 404

@app.route('/api/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 