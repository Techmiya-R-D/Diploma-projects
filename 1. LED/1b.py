import RPi.GPIO as GPIO
import time

#connect one leg of the push button to 10th pin and another leg to ground 
GPIO.setmode(GPIO.BOARD)
Button_pin = 10 #connect led pin to 10th pin of the board
Led_pin = 8     #connect led pin to 8th pin of the board

GPIO.setup(Button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Led_pin, GPIO.OUT)


try:
    while True:
        button_state = GPIO.input(Button_pin)
        
        if button_state == GPIO.LOW:
            GPIO.output(Led_pin, True)
        else:
            GPIO.output(Led_pin, False)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Terminated by user")