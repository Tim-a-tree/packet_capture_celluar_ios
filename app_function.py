from pymobiledevice3 import usbmux, lockdown, services
from device import Device

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
