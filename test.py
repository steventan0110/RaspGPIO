#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time
import temp as tp

LED = 22
LED1 = 23
Button = 12
def main():
    cpu_temp = tp.get_cpu_temp()
    gpu_temp = tp.get_gpu_temp()
    #print(gpu_temp) test if the module is used correctly
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED,GPIO.OUT)
    GPIO.setup(LED1,GPIO.OUT)
    GPIO.output(LED1, False) 
    GPIO.add_event_detect(Button, GPIO.BOTH, callback = detect, bouncetime = 200)
    while (True):
        if (cpu_temp > 40) or (gpu_temp > 40):
           GPIO.output(LED1, True) 
        pStatus(Button)
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
        
        for i in range(5):
            GPIO.output(LED, False)
            time.sleep(1)
        #destroy()
    else: 
        #do nothing
        print("Button is not pressed")
def destroy():
    GPIO.output(LED, GPIO.HIGH)
    GPIO.cleanup()
    quit()

main()
