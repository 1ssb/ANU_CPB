# Libraries needed for this:
# adafruit_bus_device
# adafruit_ahtx0.mpy

import board
import adafruit_ahtx0
from collections import deque

def delay(time_of_delay):
    import time
    # Delay by a certain time
    time.sleep(time_of_delay)

# Initialize I2C bus and sensor
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)

# Create deques with a maximum length of 10 to store recent readings
Tq = deque((), 10)
Hq = deque((), 10)

while True:
    # Read temperature and humidity from the sensor
    T, H = sensor.temperature, sensor.relative_humidity

    # Append the new readings to the respective deques
    Tq.append(T), Hq.append(H)
    
    print(list(Tq), list(Hq))
    
    delay(1)
