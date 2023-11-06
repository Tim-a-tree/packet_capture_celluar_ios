from flask import Flask, jsonify
import app_function as af
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def list_devices():
    get_devices = af.list_devices()

    json_devices = []
    for i in get_devices:
        json_devices.append(json.dumps(i.to_json()))

    return jsonify(json_devices)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
