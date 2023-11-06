from pymobiledevice3 import usbmux, lockdown, services

class Device:
    def __init__(self, name, device_type, device_serial, udid):
        self.device_name = name
        self.device_type = device_type
        self.device_serial = device_serial
        self.udid = udid

    def to_json(self):
        return {
            "device_name": self.device_name,
            "device_type": self.device_type,
            "device_serial": self.device_serial,
            "udid": self.udid
        }

def list_devices():
    devices = usbmux.list_devices()

    list_devices = []        
    for device in devices:
        client = lockdown.create_using_usbmux(device.serial)

        device_info = client.get_value(None, "DeviceName")
        device_type = client.get_value(None, "ProductType")
        device_serial = client.get_value(None, "SerialNumber")
        device_udid = client.get_value(None, "UniqueDeviceID")

        list_devices.append(Device(device_info, device_type, device_serial, device_udid))
    
    return list_devices