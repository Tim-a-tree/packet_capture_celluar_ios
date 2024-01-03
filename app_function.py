from pymobiledevice3 import usbmux, lockdown, services
from device import Device
import calendar
import time
import os

def list_devices():
    devices = usbmux.list_devices()

    list_devices = []
    for device in devices:
        client = lockdown.create_using_usbmux(device.serial)

        device_info = client.get_value(None, "DeviceName")
        device_type = client.get_value(None, "ProductType")
        device_serial = client.get_value(None, "SerialNumber")
        device_udid = client.get_value(None, "UniqueDeviceID")
        # device_build_version = client.get_value(None, "BuildVersion")
        # device_product_version = client.get_value(None, "ProductVersion")


        list_devices.append(Device(device_info, device_type, device_serial, device_udid))

    return list_devices

def set_file_name(name):
    '''
    Function : set the file name for the packet capture
    Input : name of the device
    Output : None
    '''

    global requested_file
    print("set file name function called")
    requested_file = name + "_" + str(calendar.timegm(time.gmtime())) + ".pcapng"
    print("name set with: ", requested_file)



def get_file_name():
    '''
    Function : get the file name for the packet capture
    Input : None
    Output : file name
    '''
    global requested_file
    return requested_file

def get_file_path():
    '''
    Function : get the file path for the packet capture
    Input : None
    Output : file path
    '''
    global requested_file

    file_path = os.path.join(os.getcwd(), "captures")
    file_path = os.path.join(file_path, requested_file)

    return file_path
