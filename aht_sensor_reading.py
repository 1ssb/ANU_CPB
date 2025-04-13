# Libraries needed for this:
# adafruit_bus_device
# adafruit_ahtx0.mpy

import time
import board
import adafruit_ahtx0

# Initialize I2C bus and sensor
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    temperature = sensor.temperature
    humidity = sensor.relative_humidity
    print(f"Temperature: {temperature:.1f} °C")
    print(f"Humidity: {humidity:.1f} %")
    time.sleep(1)  # Prints the result every 1 second
    # How  to plot: https://codewith.mu/en/tutorials/1.2/plotter
    print((temperature, humidity), )
