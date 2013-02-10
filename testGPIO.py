import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

i = 0

try:
    while True:
        i += 1
        if i % 2 == 0:
            GPIO.output(13, True)
            print('Output High')

        else:
            GPIO.output(13, False)
            print('Output Low')
            
        sleep(0.5)
        
except KeyboardInterrupt:
    pass
