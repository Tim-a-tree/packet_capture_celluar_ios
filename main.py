from sys import platform
import pymobiledevice3.usbmux

def main():
    # gets the list of connected device
    # NOTE: only shows number, udid, type 
    list_device = pymobiledevice3.usbmux.list_devices()

    print(list_device)

    # gets the UDID of the device
    # WARNING: only gets the first device from the list, it will be updated later
    print("UDID: ", list_device[0].serial)

    # TODO: connect to the device and start capturing the packets



if __name__ == "__main__":
    main()
