from agents import DroneAgent

class DroneEnv:
    def __init__(self, targets):
        self.drones = [DroneAgent("Drone1", 0), DroneAgent("Drone2", 0)]
        self.targets = targets
        self.steps = 0

    def step(self):
        for i, drone in enumerate(self.drones):
            drone.move_towards(self.targets[i])
        self.steps += 1
        done = all(drone.pos == self.targets[i] for i, drone in enumerate(self.drones))
        return done
