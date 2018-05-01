import readchar
import RPi.GPIO as gpio
import time
 

PIN_PWM1 = 12
PIN_PWM2 = 18

PIN_MOTOR1P = 23
PIN_MOTOR1N = 24
PIN_MOTOR2P = 17
PIN_MOTOR2N = 22

gpio.setmode(gpio.BCM)

gpio.setup(PIN_MOTOR2P, gpio.OUT)
gpio.setup(PIN_MOTOR2N, gpio.OUT)
gpio.setup(PIN_MOTOR1P, gpio.OUT)
gpio.setup(PIN_MOTOR1N, gpio.OUT)

# pwm pins
gpio.setup(PIN_PWM2, gpio.OUT) # right motor
gpio.setup(PIN_PWM1, gpio.OUT) # left motor
pwml = gpio.PWM(PIN_PWM1, 100)
pwmr = gpio.PWM(PIN_PWM2, 100)
pwms = [pwml, pwmr]

pwml.start(0)
pwmr.start(0)

def stop(x = True,y = True):
    for pwm in pwms:
        pwm.ChangeDutyCycle(0)
    #gpio.output(PIN_PWM1, False)
    #gpio.output(PIN_PWM2, False)


def init(x = True,y = True): 
    dc = 70
    dc2 = 30
    if x:
        pwml.ChangeDutyCycle(dc)
    if y: 
        pwmr.ChangeDutyCycle(dc)



def motor1_rev():
    gpio.output(PIN_MOTOR1P, True)
    gpio.output(PIN_MOTOR1N, False)

def motor1_for():
    gpio.output(PIN_MOTOR1P, False)
    gpio.output(PIN_MOTOR1N, True)

def motor2_rev():
    gpio.output(PIN_MOTOR2P, True)
    gpio.output(PIN_MOTOR2N, False)

def motor2_for():
    gpio.output(PIN_MOTOR2P, False)
    gpio.output(PIN_MOTOR2N, True)


def reverse(tf):
 init()
 motor1_rev()
 motor2_rev()
 time.sleep(tf)
 stop()

def forward(tf):
 init()
 motor1_for()
 motor2_for()
 time.sleep(tf)
 stop()

def left(tf):
 init(True, False)
 motor1_for()
 time.sleep(tf)
 stop()

def right(tf):
 init(False, True)
 motor2_for()
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
