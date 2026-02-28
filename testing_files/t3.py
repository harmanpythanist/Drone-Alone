import time
from dronekit import connect, VehicleMode

connection_string = "udp:127.0.0.1:1450"
vehicle = connect(connection_string, wait_ready=True)

# Wait until ready
while not vehicle.is_armable:
    print("Waiting to become armable...")
    time.sleep(1)

# Set GUIDED mode
vehicle.mode = VehicleMode("GUIDED")

while vehicle.mode.name != "GUIDED":
    print("Waiting for GUIDED mode...")
    time.sleep(1)

# Arm
vehicle.armed = True

while not vehicle.armed:
    print("Waiting for arming...")
    time.sleep(1)

# Takeoff
print("Taking off!")
vehicle.simple_takeoff(5)

time.sleep(10)

# Land
print("Landing...")
vehicle.mode = VehicleMode("LAND")

time.sleep(10)

vehicle.close()