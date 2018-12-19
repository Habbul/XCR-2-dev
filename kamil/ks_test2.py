import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(3,GPIO.IN)
i=1;
while i < 30:
    if GPIO.input(3)==False:
        GPIO.output(7,1)
    else:
        GPIO.output(7,0)
    print(i)
    i+=1
