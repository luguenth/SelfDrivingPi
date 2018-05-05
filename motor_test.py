import RPi.GPIO as gpio
import math


class HBridge:
    PIN_PWM1 = 12
    PIN_PWM2 = 18

    PIN_MOTOR1P = 23
    PIN_MOTOR1N = 24
    PIN_MOTOR2P = 17
    PIN_MOTOR2N = 22

    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.setupMotors()
        self.setupPWM()
        self.startPWM()

    def setupMotors(self):
        gpio.setup(self.PIN_MOTOR2P, gpio.OUT)
        gpio.setup(self.PIN_MOTOR2N, gpio.OUT)
        gpio.setup(self.PIN_MOTOR1P, gpio.OUT)
        gpio.setup(self.PIN_MOTOR1N, gpio.OUT)

    def setupPWM(self):
        gpio.setup(self.PIN_PWM2, gpio.OUT)  # right motor
        gpio.setup(self.PIN_PWM1, gpio.OUT)  # left motor
        self.pwml = gpio.PWM(self.PIN_PWM1, 100)
        self.pwmr = gpio.PWM(self.PIN_PWM2, 100)

    def startPWM(self):
        self.pwml.start(0)
        self.pwmr.start(0)

    def stopPWM(self):
        self.pwml.stop(0)
        self.pwmr.stop(0)

    """
    This function is using a 2 Dimensional Vector to determinate the
    direction you want to go. For Example:
    Vector(x=0,y=1) would drive in a straight line.
    (sqrt(2)/2, sqrt(2)/2)  => right forward    -> full powered
    (-sqrt(2)/2, sqrt(2)/2) => left Forward     -> full powered
    (0,0.5)                 => forward          -> half powered
    (1, 0)                  => right            -> without motion in the right wheels
    """
    def dutyCycleMatrix(self, vector):

        # Controller Joysticks would be to sensitive (tested with xBox360)
        # Just for debugging with Controllers
        if(abs(vector[0]) > 0.5):
            x = vector[0]
        else:
            x = 0
        if(abs(vector[1]) > 0.5):
            y = vector[1]
        else:
            y = 0

        # Calculating  the angle of the vector do determine the direction
        if x is 0:
            angle = 0
        else:
            angle = math.atan(y/x)*100

        # Calculating the length of the vector
        length = math.sqrt(y*y+x*x)
        # the four different directions
        print("Angle: " + str(angle) + "; Length: " + str(length))
        # Forward Right
        if angle < 90:
            left = length*100
            if left > 100:
                left = 100
            elif left < 0:
                left = 0
            right = angle
            if right > 100:
                right = 100
            elif right < 0:
                right = 0
            self.motor1_for()
            self.motor2_for()
            self.pwml.ChangeDutyCycle(left)
            self.pwmr.ChangeDutyCycle(right)

        # Forward Left
        elif angle < 180:
            self.motor1_for()
            self.motor2_for()
            self.pwml.ChangeDutyCycle(length)
            self.pwmr.ChangeDutyCycle(abs(100 - 100/90*(angle-90)*length))

        # Reverse Left
        elif angle < 270:
            self.motor1_rev()
            self.motor2_rev()
            self.pwml.ChangeDutyCycle(length)
            self.pwmr.ChangeDutyCycle(abs((100/90*angle-180)*length))

        # Reverse Right
        elif angle < 360:
            self.motor1_rev()
            self.motor2_rev()
            self.pwml.ChangeDutyCycle(length)
            self.pwmr.ChangeDutyCycle(abs(100 - 100/90*(angle-270)*length))

    def defineDutyCycle(self, x=100, y=100):
        dc = 70
        if x:
            self.pwml.ChangeDutyCycle(dc)
        if y:
            self.pwmr.ChangeDutyCycle(dc)

    def motor1_rev(self):
        gpio.output(self.PIN_MOTOR1P, True)
        gpio.output(self.PIN_MOTOR1N, False)

    def motor1_for(self):
        gpio.output(self.PIN_MOTOR1P, False)
        gpio.output(self.PIN_MOTOR1N, True)

    def motor2_rev(self):
        gpio.output(self.PIN_MOTOR2P, True)
        gpio.output(self.PIN_MOTOR2N, False)

    def motor2_for(self):
        gpio.output(self.PIN_MOTOR2P, False)
        gpio.output(self.PIN_MOTOR2N, True)

    def shutdown(self):
        self.stopPWM()
        gpio.cleanup()
