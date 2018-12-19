import RPi.GPIO as GPIO
import time
import signal
import sys
import MotionController
#  Here the sonar sleeps 2 seconds and then dive us the measurement in cm.
#  We can change sleep time by modifying time.sleep(2) function.
#  The measurement have error delta approx. 0.5 - 1 cm.

GPIO.setmode(GPIO.BOARD)
# set GPIO Pins
pinTrigger = 13
pinEcho = 15

def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup() 
	sys.exit(0)

signal.signal(signal.SIGINT, close)

# set GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

def checkDistance(arg):
        for i in range(10):
                arg.AddNeuron(4)
        while True:
                #print "hahah"
                GPIO.output(pinTrigger, True)
                # set Trigger after 0.01ms to LOW
                time.sleep(0.00001)
                GPIO.output(pinTrigger, False) #  this is need to turn on the sonar
                #print "2"

                startTime = time.time()
                stopTime = time.time()
                #print "3"
                
                # save start time
                while 0 == GPIO.input(pinEcho):
                        startTime = time.time()
                #print "4"
                # save time of arrival
                while 1 == GPIO.input(pinEcho):
                        stopTime = time.time()
                #print "5"       
                # time difference between start and arrival
                TimeElapsed = stopTime - startTime
                # multiply with the sonic speed (34300 cm/s)
                # and divide by 2, because there and back
                distance = TimeElapsed * 17000
                # (TimeElapsed * 34300) / 2
                print ("Distance: %.2f",distance," cm")
                if(distance < 100):
                   arg.SpikeProcessing(4, int(distance%23))
                time.sleep(0.2)
