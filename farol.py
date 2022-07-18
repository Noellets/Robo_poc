import time
from datetime import datetime
import RPi.GPIO as GPIO

#Variáveis
led01 = 1       #porta 1
led02 = 2       #porta 2
led03 = 3       #porta 3
ledout1 = 5     #GPIO5
ledout2 = 6     #GPIO6
ledout3 = 13    #GPIO13


def setup_raspberry():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledout1, GPIO.OUT)
    GPIO.setup(ledout2, GPIO.OUT)
    GPIO.setup(ledout3, GPIO.OUT)

def aciona_led(led, status):
    if led == led01:
        if status == True:
            GPIO.output(ledout1, GPIO.HIGH)
        else:
            GPIO.output(ledout1, GPIO.LOW)
    elif led == led02:
        if status == True:
            GPIO.output(ledout2, GPIO.HIGH)
        else:
            GPIO.output(ledout2, GPIO.LOW)
    elif led == led03:
        if status == True:
            GPIO.output(ledout3, GPIO.HIGH)
        else:
            GPIO.output(ledout3, GPIO.LOW)
    else:
        print("Led inexistente!")

def apaga_todos_leds():
    for led in range(1, 4):     #valor inicial é 1
        aciona_led(led, False)
        print("Apagando led: ", led)




   




