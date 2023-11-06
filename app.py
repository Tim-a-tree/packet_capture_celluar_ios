from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/list/devices', methods=['GET'])
def list_devices():
    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)
