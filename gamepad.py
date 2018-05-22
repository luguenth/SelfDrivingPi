"""
Gamepad Module
Daniel J. Gonzalez
dgonz@mit.edu

Based off code from: http://robots.dacloughb.com/project-1/logitech-game-pad/
"""

import pygame

class GamepadCtrl:

    j = None
    
    pygame.init()
    j = pygame.joystick.Joystick(0)
    j.init()
    print('Initialized Joystick : %s' % j.get_name())
    
    def __init__(self):
        pass

    """
    Returns a vector of the following form:
    [LThumbstickX, LThumbstickY, Unknown Coupled Axis???,
    RThumbstickX, RThumbstickY,
    Button 1/X, Button 2/A, Button 3/B, Button 4/Y,
    Left Bumper, Right Bumper, Left Trigger, Right Triller,
    Select, Start, Left Thumb Press, Right Thumb Press]
    
    Note:
    No D-Pad.
    Triggers are switches, not variable.
    Your controller may be different
    """
    
    def get(self):
        out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        it = 0 #iterator
        pygame.event.pump()
    
        #Read input from the two joysticks
        for i in range(0, self.j.get_numaxes()):
            out[it] = self.j.get_axis(i)
            it+=1
        #Read input from buttons
        for i in range(0, self.j.get_numbuttons()):
            out[it] = self.j.get_button(i)
            it+=1
        #print(out)
        return out[0], out[2], out[5]
