import readchar
import RPi.GPIO as gpio
import time
 

PIN_PWM1 = 12
PIN_PWM2 = 18

gpio.setmode(gpio.BCM)

gpio.setup(17, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)

# pwm pins
gpio.setup(PIN_PWM2, gpio.OUT) # right motor
gpio.setup(PIN_PWM1, gpio.OUT) # left motor
pwml = gpio.PWM(PIN_PWM1, 100)
pwmr = gpio.PWM(PIN_PWM2, 100)
pwms = [pwml, pwmr]

pwml.start(0)
pwmr.start(0)

def stop():
    for pwm in pwms:
        pwm.ChangeDutyCycle(0)
    #gpio.output(PIN_PWM1, False)
    #gpio.output(PIN_PWM2, False)


def init(): 
    for pwm in pwms:
        pwm.ChangeDutyCycle(20)
    #gpio.output(PIN_PWM1, True)
    #gpio.output(PIN_PWM2, True)


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
    
for pwm in pwms:
    pwm.stop()
gpio.cleanup()
