
# export FLASK_APP=server.py && flask run --host=0.0.0.0
from flask import Flask, request
app = Flask(__name__)

@app.route('/key-topics', methods=['POST'])
def hello_world():
    data = request.json()
    print(data.raw_text)
    output = ['test', 'output']
    return jsonify(output)