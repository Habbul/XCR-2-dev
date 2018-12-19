import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

while True:
    if (GPIO.input(12) == False) and (GPIO.input(16) == True):
          print "btn 12 was pressed"
          GPIO.output(18,1)
          GPIO.output(22,0)
    else:
            if (GPIO.input(12) == True) and (GPIO.input(16) == False):
                  print "btn 16 was pressed"  
                  GPIO.output(22,1)
                  GPIO.output(18,0)
            else:
                    if (GPIO.input(12) == True) and (GPIO.input(16) == True):
                          print "you do nothing with btns"
                          GPIO.output(22,0)
                          GPIO.output(18,0)
                    else:
                            if (GPIO.input(12) == False) and (GPIO.input(16) == False):
                                  print "pressing two buttons at the same time is not allowed"
                                  GPIO.output(22,0)
                                  GPIO.output(18,0)
