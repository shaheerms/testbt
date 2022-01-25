import bluetooth

def finddevices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))

    return nearby_devices

def connectdevice(addr):
    s = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    s.connect((addr,1))

