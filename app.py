from flask import Flask, jsonify, request
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

#global variable
file_name = ""



@app.route('/', methods=['GET'])
# returns a list of devices connected to the computer
def list_devices():
    get_devices = af.list_devices()
    get_devices = [dv.to_json(device) for device in get_devices]
    return jsonify(get_devices)


@app.route("/<udid>", methods=['POST'])
# requests a packet capture from the device
def get_packet(udid):
    parsed_json = json.loads(request.data.decode('utf-8'))
    udid = parsed_json.get('device_udid')
    device_name = parsed_json.get('device_name')

    print("UDID: ", udid)
    print("Device Name: ", device_name)

    af.set_file_name(device_name)
    rvi.start_capture(udid, file_name)

    return jsonify({"message": "Started capture with file name: " + af.get_file_name()})

@socketio.on('message')
def handle_message(message):
    print("")

@app.route("/stop/<udid>", methods=['GET'])
# stops the packet capture
def stop_packet(udid):

    rvi.stop_capture()

    return jsonify({"message": "Stopped capture", "file_name": af.get_file_name()})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
