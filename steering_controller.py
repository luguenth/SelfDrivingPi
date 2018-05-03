from gamepad import GamepadCtrl
from motor_test import HBridge

car = HBridge()
ctrl = GamepadCtrl()

while True:
    x, y = ctrl.get()
    car.dutyCycleMatrix([x, y])
car.shutdown()
