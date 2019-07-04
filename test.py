#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time
LED = 21
Button = 5
def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED,GPIO.OUT)
    GPIO.add_event_detect(Button, GPIO.BOTH, callback = detect, bouncetime = 200)
    while (True):
        #pStatus(Button)
        GPIO.output(LED,True)
        time.sleep(0.5)
        GPIO.output(LED,False)        
        time.sleep(0.5)

def pStatus(channel): 
    if GPIO.input(channel):   
        print('Input was HIGH')
    else:
        print('Input was LOW')

def detect(chn):
    if (GPIO.input(Button)):
        print("Button is pressed")
        destroy()
    else: 
        #do nothing
        print("Button is not pressed")
def destroy():
    GPIO.output(LED, GPIO.LOW)
    GOPI.cleanup()
main()