from flask import Flask, jsonify
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

@app.route('/api/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 