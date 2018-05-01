import readchar
import RPi.GPIO as gpio
import time
 

gpio.setmode(gpio.BCM)

gpio.setup(17, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)

# pwm pins
gpio.setup(35, gpio.OUT) # left motor
gpio.setup(25, gpio.OUT) # right motor
gpio.setup(0, gpio.OUT) # right motor
pwml = gpio.PWM(0, 1)
pwmr = gpio.PWM(0, 1)
pwms = [pwml, pwmr]


def stop():
    #gpio.cleanup()
    for pwm in pwms:
        pwm.stop()


def init(): 
    pwml.start(100)
    pwmr.start(50)


def reverse(tf):
 init()
 gpio.output(17, True)
 gpio.output(22, False)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(tf)
 stop()

def forward(tf):
 init()
 gpio.output(17, False)
 gpio.output(22, True)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(tf)
 stop()

def left(tf):
 init()
 gpio.output(17, 0)
 gpio.output(22, 1)
 gpio.output(23, 1)
 gpio.output(24, 1)
 time.sleep(tf)
 stop()

def right(tf):
 init()
 gpio.output(17, 1)
 gpio.output(22, 1)
 gpio.output(23, 0) 
 gpio.output(24, 1)
 time.sleep(tf)
 stop()


read = 0

while(1):
    read = readchar.readchar()
    if (read is 'w'):
        forward(0.1)
    if (read is 's'):
        reverse(0.1)
    if (read is 'a'):
        left(0.1)
    if (read is 'd'):
        right(0.1)
    if (read is 'q'):
        break
    
gpio.cleanup()
