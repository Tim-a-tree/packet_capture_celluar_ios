class Device:
    def __init__(self, name, device_type, device_serial, udid):
        self.device_name = name
        self.device_type = device_type
        self.device_serial = device_serial
        self.udid = udid

def to_json(Device):
    return {
        "device_name": Device.device_name,
        "device_type": Device.device_type,
        "device_serial": Device.device_serial,
        "udid": Device.udid
    }
