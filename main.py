from sys import platform
from pymobiledevice3 import usbmux, lockdown, services
import rvi_capture_copy as rvi
import time
import calendar


# TODO: changing the packet capture algorithm with C code (using libimobiledevice)


# auto-detection
def auto_detect():
    devices = usbmux.list_devices()

    return devices


def main():
    # if no device is connected, wait until the device is connected
    while True:
        device_name = auto_detect()
        if len(device_name) == 0:
            print("waiting to connect the devices......")
            time.sleep(1)
        else:
            break

    # gets the list of connected device
    # NOTE: only shows number, udid, type
    print("----------------- Connected Devices -----------------")
    for i in range(len(device_name)):
        print(i, device_name[i].serial)

    print("Select the device from the list:")
    device_num = int(input())
    udid = device_name[device_num].serial
    print("UDID: ", udid)

    client = lockdown.create_using_usbmux(udid)

    device_info = client.get_value(None, "DeviceName")
    device_type = client.get_value(None, "ProductType")
    device_serial = client.get_value(None, "SerialNumber")
    device_udid = client.get_value(None, "UniqueDeviceID")

    file_name = device_info + "_" + str(calendar.timegm(time.gmtime())) + ".pcapng"

    # live capture option
    print("Live Capture?(Y/N)")
    live = input()

    print(
        "Start Capturing the packets from the device, in order to stop the capture press 'Ctrl + C'\n\n"
    )

    if live.lower() == "y":
        rvi.start_live_capture(udid, file_name)
    else:
        rvi.start_capture(udid, file_name)


if __name__ == "__main__":
    main()
