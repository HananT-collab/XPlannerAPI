from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])

def home():
    return jsonify({"message": "Welcome to XPlanner API!"})

if __name__ == '__main__':
    app.run(debug=True)  # Run the app with debug mode enabled