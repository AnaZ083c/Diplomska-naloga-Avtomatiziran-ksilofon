import bluetooth
import sys

bd_addr = "00:21:13:01:1F:14"

port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
print('Connected')
# sock.settimeout(1.0)

count = 0
while count < 10:
    data = sock.recv(12)
    print('received: %s' % data)

    count += 1

sock.close()
