import RPi.GPIO as gpio


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

    def drive(self, steer, velo):
        if velo > 0:
            self.motor1_for()
            self.motor2_for()
        elif velo < 0:
            self.motor1_rev()
            self.motor2_rev()
        velo = abs(velo)*100
        steer_l = min(1, 1 - steer)
        steer_r = min(1, 1 + steer)
        print(steer_l*velo, steer_r*velo)
        self.pwml.ChangeDutyCycle(steer_l*velo)
        self.pwmr.ChangeDutyCycle(steer_r*velo)

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
