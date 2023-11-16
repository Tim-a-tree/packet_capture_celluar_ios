from flask import Flask, jsonify, request, make_response
import app_function as af
import json
from flask_cors import CORS
from flask_socketio import SocketIO, send
import rvi_capture_copy as rvi
import datetime
import calendar
import device as dv
from threading import Thread
from multiprocessing import Process
import ctypes

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# socketio = SocketIO(app, cors_allowed_origins="*")

#global variable
requested_file = ""
process_list = []



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

    p = Process(target=rvi.start_capture, args=(udid, af.get_file_name(),))
    p.daemon = True
    p.start()
    process_pid = p.pid
    print("Process started", p.pid)
    process_list.append(process_pid)
    print("Process list updated:", process_list)

    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    response = jsonify({"message": "Started capture", "file_name": af.get_file_name()})


    print("end of get packet function")
    return response



@app.route("/stop/<udid>", methods=['GET'])
# stops the packet capture
def stop_packet(udid):

    print("stop packet function called")
    print("Process list:", process_list)

    process_pid = process_list.pop()
    rvi.stop_capture(process_pid)

    return jsonify({"message": "Stopped capture", "file_name": af.get_file_name()})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
