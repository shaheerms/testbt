
import bluetooth
import sys
bl = bluetooth
print("Scanning for 10 seconds...")
b = bl.discover_devices(lookup_names=True)
for name, addr in b:
    print(f"{addr}, Scanning for 10 seconds...{name}")

a = bl.find_service()
for p in a:
    print(f'{p["host"]}')
add = '40:91:51:B1:A8:9E'


service_matches = bluetooth.find_service( address = add )

if len(service_matches) == 0:
    print ("couldn't find the FooBar service")

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print ("connecting to \"%s\" on %s" % (name, host))

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((host, port))
sock.send("hello!!")
sock.close()