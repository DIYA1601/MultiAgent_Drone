import numpy as np

class DroneAgent:
    def __init__(self, name, start_pos):
        self.name = name
        self.pos = start_pos

    def move_towards(self, target):
        self.pos += np.sign(target - self.pos)
        return self.pos
