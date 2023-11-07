from flask import Flask, jsonify
import app_function as af
import json
from flask_cors import CORS
from flask_socketio import SocketIO, send
import rvi_capture_copy as rvi
import datetime
import calendar
import device as dv

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/', methods=['GET'])
def list_devices():
    get_devices = af.list_devices()
    get_devices = [dv.to_json(device) for device in get_devices]
    return jsonify(get_devices)

@app.route("/<name>/<udid>", methods=['GET'])
def get_packet(udid, name):
    file_name = name + "_" + calendar.timegm(time.gmtime()) + ".pcapng"
    rvi.start_live_capture(udid, file_name)

@socketio.on('message')
def handle_message(message):
    print("")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
