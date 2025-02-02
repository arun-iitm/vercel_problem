from flask import Flask, request, jsonify
import json
import os
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

# Load marks data from JSON file
data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'q-vercel-python.json')
with open(data_file, 'r') as f:
    marks_full_list = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('names')
    marks_list = []
    for name in names:
        # Find the marks for the given name, or return 0 if not found
        mark = next((student["marks"] for student in marks_full_list if student["name"] == name), 0)
        marks_list.append(mark)
    
    return jsonify({"marks": marks_list})

if __name__ == '__main__':
    app.run(debug=True)