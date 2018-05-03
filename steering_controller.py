import gamepad
from motor_test import HBridge

car = HBridge()

while True:
    x, y = gamepad.get()
    car.dutyCycleMatrix(x, y)
car.stop()
