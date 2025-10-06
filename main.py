from environment import DroneEnv

targets = [5, 10]
env = DroneEnv(targets)

done = False
while not done:
    done = env.step()
    positions = [drone.pos for drone in env.drones]
    print("Drone Positions:", positions)

print("All drones reached targets in", env.steps, "steps.")
