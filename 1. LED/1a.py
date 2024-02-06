import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)

try:
    while True:
        GPIO.output(10, True) #connect the pin to 10th pin of Board and ground pin to 6th pin 
        time.sleep(2)
        GPIO.output(10, False)
        time.sleep(2)  
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Stopped by User")
