import serial
import time

usbCom = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(2)

blocked = False


def Process(group, neuron, spiked, blocked):
    print("Processing " + str(len(spiked)))
    for elem in spiked:
        if(elem.groupId == 3):
            if(elem.Id == 0 and not blocked):
                feelPleasure()
            if(elem.Id == 1 and not blocked):
                feelPain()
				
def feelPleasure(blocked):
		change_state(blocked)
		usbCom.open
		usbCom.write(b'1')
		usbCom.close
		change_state(blocked)
		
    
def feelPain(blocked):
		change_state(blocked)
		usbCom.open
		usbCom.write(b'2')
		usbCom.close
		change_state(blocked)
		

def turnToLeft():
		usbCom.open
		usbCom.write(b'3')
		usbCom.close
		

def turnToRight():
		usbCom.open
		usbCom.write(b'4')
		usbCom.close
		

def stop():
		usbCom.open
		usbCom.write(b'0')
		usbCom.close
		
def change_state(blocked):
                blocked =not blocked
                print(blocked)
                
def curiosity(blocked):
                change_state(blocked)
                stop()
                time.sleep(3)
                print("lol")
                change_state(blocked)
                turnToLeft()
                time.sleep(2)
                usbCom.open
                usbCom.write(b'1')
                usbCom.close
                time.sleep(2)
		
    
"""Groups:
1 - visual
2 - audio
3 - gripper ?
4 - p&p
"""

"""Groups:
1 - visual
2 - audio
3 - gripper ?
4 - p&p 0 - pleasure 1- pain
"""
