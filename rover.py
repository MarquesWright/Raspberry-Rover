import time  # Import the Time library
from gpiozero import CamJamKitRobot, DistanceSensor  # Import the GPIO Zero Libraries

# Define GPIO pins to use for the distance sensor
pinTrigger = 17
pinEcho = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo = pinEcho, trigger = pinTrigger)

# Distance Variables
hownear = 15.0
forward_time = 1 
reverse_time = 1
turn_time = 0.75

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.4
rightmotorspeed = 0.4

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (-leftmotorspeed, rightmotorspeed)
motorright = (leftmotorspeed, -rightmotorspeed)


# Return True if the ultrasonic sensor sees an obstacle
def isnearobstacle(localhownear):
    distance = sensor.distance * 100

    print("IsNearObstacle: " + str(distance))
    if distance < localhownear:
        return True
    else:
        return False


# Move back a little, then turn right
def avoidobstacle():
    # Back off a little
    print("Backwards")
    robot.value = motorbackward
    time.sleep(reverse_time)
    robot.stop()

    # Turn right
    print("Right")
    robot.value = motorright
    time.sleep(turn_time)
    robot.stop()


# Move forward a little, then turn left
def backontrack():
    # Forward a little
    print("Forward")
    robot.value = motorforward
    time.sleep(forward_time)
    robot.stop()

    # Turn left
    print("Left")
    robot.value = motorleft
    time.sleep(turn_time)
    robot.stop()

# Your code to control the robot goes below this line
try:
    # repeat the next indented block forever
    while True:
        robot.value = motorforward
        time.sleep(0.1)
        if isnearobstacle(hownear):
            robot.stop()
            avoidobstacle()
            backontrack()
            print("Forward")


# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    robot.stop()
