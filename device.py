class Device:
    def __init__(self, name, device_type, device_id, device_udid):
        self.device_name = name
        self.device_type = device_type
        self.device_id = device_id
        self.device_udid = device_udid
        # self.build_version = build_version
        # self.product_version = product_version

def to_json(Device):
    return {
        "device_name": Device.device_name,
        "device_type": Device.device_type,
        "device_id": Device.device_id,
        "device_udid": Device.device_udid,
        # "build_version": Device.build_version,
        # "product_version": Device.product_version

    }


