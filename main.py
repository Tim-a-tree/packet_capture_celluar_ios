from sys import platform
from pymobiledevice3 import usbmux, lockdown, services
import rvi_capture_copy as rvi

# WARNING: on development,
# def get_interface(udid):
#     # get the lockdown client for the first connected device
#     client = lockdown.create_using_usbmux()

#     # get the network information
#     network_info = client.get_value("com.apple.mobile.data_sync", "com.apple.mobile.wireless_lockdown", "WiFiNetworkInfo", udid)


#     # extract the interface name
#     interface = network_info["InterfaceName"]
    

#     return interface

# auto-detection
# def auto_detect():


# NOTE: currently only detects when the device is connected
# TODO: if the device is not connected, wait for the device to be connected
# TODO: realtime packet capture
# TODO: changing the packet capture algorithm with C code (using libimobiledevice)
# TODO: able to select the device from the multiple devices

def main():
    # gets the list of connected device
    # NOTE: only shows number, udid, type 
    device_name = usbmux.list_devices()
    if len(device_name) == 0:
        print("Please connect the device and start the program again")
        input("Press enter to exit;")
        quit()

    print(device_name)
    udid = device_name[0].serial
    print("UDID: ", udid) # WARNING: only gets the first device from the list, it will be updated later
    # print(get_interface(udid))

    file_name = input("Please enter the name of the file: ")
    file_name = file_name + ".pcapng"
    print("\n\nStart Capturing the packets from the device, in order to stop the capture press 'Ctrl + C'\n\n")
    rvi.start_capture(udid, file_name)



if __name__ == "__main__":
    main()
