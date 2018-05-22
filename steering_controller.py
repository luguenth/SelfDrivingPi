from gamepad import GamepadCtrl
from motor_test import HBridge

car = HBridge()
ctrl = GamepadCtrl()

while True:
    x, lt, rt = ctrl.get()
    velo = (-lt-1 + rt+1)/2
    car.drive(x, velo)
car.shutdown()
