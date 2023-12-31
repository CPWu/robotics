from cortano import RemoteInterface

if __name__ == "__main__":
  robot = RemoteInterface("192.168.87.130")
  while True:
    robot.update()
    color, depth, sensors = robot.read()
 
    forward = robot.keys["w"] - robot.keys["s"]
    robot.motor[0] = -forward * 64
    robot.motor[9] = forward * 64