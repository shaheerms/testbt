from bluetoothctl import Bluetoothctl
import time

def finddevices():
        bl = Bluetoothctl()
        bl.start_scan()
        print("Scanning for 10 seconds...")
        for i in range(0, 10):
            print(i)
            time.sleep(1)
        nearby_devices = bl.get_discoverable_devices()
        print(nearby_devices)
        return nearby_devices



