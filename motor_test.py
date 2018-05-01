import readchar
import RPi.GPIO as gpio
import time


def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)


def reverse(tf):
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(tf)
    gpio.cleanup()


def forward(tf):
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tf)
    gpio.cleanup()


def left(tf):
    init()
    gpio.output(17, 0)
    gpio.output(22, 1)
    gpio.output(23, 1)
    gpio.output(24, 1)
    time.sleep(tf)
    gpio.cleanup()


def right(tf):
    init()
    gpio.output(17, 1)
    gpio.output(22, 1)
    gpio.output(23, 0)
    gpio.output(24, 1)
    time.sleep(tf)
    gpio.cleanup()


read = 0

while(1):
    read = readchar.readchar()
    if (read is 'w'):
        forward(0.1)
    if (read is 's'):
        reverse(0.1)
    if (read is 'a'):
        print('left')
        left(0.1)
    if (read is 'd'):
        right(0.1)
    if (read is 'q'):
        break
