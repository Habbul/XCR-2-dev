import serial
import time

usbCom = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(2)   # after connection to COM port arduino is restart. So need to wait

usbCom.open
usbCom.write(b'0')
usbCom.close
