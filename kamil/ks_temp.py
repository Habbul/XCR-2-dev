import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

while True:
    if (GPIO.input(12) == True):
          GPIO.output(18,0)
          GPIO.output(22,0)
