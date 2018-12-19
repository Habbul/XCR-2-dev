from time import sleep     
import RPi.GPIO as GPIO 
import MotionController
   
GPIO.setmode(GPIO.BOARD)   
button1=16                 # Button 1 pin 16 green, pleasure
button2=12                 # Button 2 pin 12 red, pain
LED1=22                    # LED 1 GREEN pleasure pin 22
LED2=18                    # LED 2  RED  pain pin 18
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 
GPIO.setup(LED1,GPIO.OUT,) 
GPIO.setup(LED2,GPIO.OUT)  
BS1=False                  
BS2=False   
print("hello")
GPIO.output(LED1,False)
GPIO.output(LED2,False)               
def checkPleasure(arg):
        arg.AddNeuron(3);
        arg.AddNeuron(3);
        while(1):                
                if GPIO.input(button1)==0:            # if button 1 press
                        print("Button 1 Was Pressed:")
                        if BS1==False:                # If the LED is off
                                GPIO.output(LED1,True)# turn on LED 1
                                BS1=True             # Set Flag to show LED1 is now On
                                arg.SpikeProcessing(3, 0)
                                if(not MotionController.blocked):
                                        MotionController.feelPleasure(MotionController.blocked)                                 
                else:                         # If the LED is on
                        GPIO.output(LED1,False) # Turn LED 1 off
                        BS1=False               # Set Flag to show LED1 is now Off
                if GPIO.input(button2)==0: #Repeat for LED 2 and button 2
                        print("Button 2 Was Pressed:")
                        if BS2==False:
                                GPIO.output(LED2,True)
                                BS2=True
                                arg.SpikeProcessing(3, 1)
                                if(not MotionController.blocked):
                                        MotionController.feelPain(MotionController.blocked)                
                else:                         # If the LED is on
                        GPIO.output(LED2,False) # Turn LED 1 off
                        BS2=False                
               
                BS1=False
                BS2=False   

                sleep(0.2)
			    
