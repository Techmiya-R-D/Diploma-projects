import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relaypin = 20 #connect to pin 38
Button_pin = 4 # connect to pin 7

GPIO.setup(Button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(relaypin, GPIO.OUT)

try:
    while True:
        button_state = GPIO.input(Button_pin)
        
        if button_state == GPIO.LOW:
            GPIO.output(relaypin, GPIO.LOW)
        else:
            GPIO.output(relaypin, GPIO.HIGH)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Terminated by user")