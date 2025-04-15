# This is an implementation of the greenhouse sensing model which shows basic signals modelling the temperature and humidity from the last 10 readings
# These 10 values are to be updated dynamically. Remember that your board will not have enough memory to store every value, so if you incorrectly try to register and store everything,
# it will run out of memmory and stop working. Hence, the deque is essential.

import time
import board
import neopixel
import adafruit_ahtx0
from collections import deque

# Setup
NUM_PIXELS = 10
BRIGHTNESS = 0.3
UPDATE_EVERY = 5  # seconds
HISTORY_SIZE = 10

# Pixel groups
TEMP_UP = [0, 1]
TEMP_DOWN = [2, 3]
HUMID_UP = [4, 5]
HUMID_DOWN = [6, 7]

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

# Hardware
pixels = neopixel.NeoPixel(board.NEOPIXEL, NUM_PIXELS, brightness=BRIGHTNESS)
sensor = adafruit_ahtx0.AHTx0(board.I2C())

# Store past readings
temps = deque((), HISTORY_SIZE)
hums = deque((), HISTORY_SIZE)
prev_temp = None
prev_hum = None

# Blink some LEDs
def blink(indices, color):
    for _ in range(3):
        for i in indices:
            pixels[i] = color
        time.sleep(0.2)
        for i in indices:
            pixels[i] = OFF
        time.sleep(0.2)


# Show a change
def show_change(kind, going_up):
    pixels.fill(OFF)
    if kind == "temp":
        if going_up:
            blink(TEMP_UP, RED)
        else:
            blink(TEMP_DOWN, BLUE)
    elif kind == "hum":
        if going_up:
            blink(HUMID_UP, GREEN)
        else:
            blink(HUMID_DOWN, YELLOW)


# Start
start_time = time.monotonic()
last_update = start_time

while True:
    now = time.monotonic()
    temp = sensor.temperature
    hum = sensor.relative_humidity

    # Flash white during first 10 seconds
    if now - start_time < 10:
        pixels.fill(WHITE)
    else:
        pixels.fill(OFF)

    temps.append(temp)
    hums.append(hum)

    # Every few seconds, check for change
    if now - last_update >= UPDATE_EVERY:
        avg_temp = sum(temps) / len(temps)
        avg_hum = sum(hums) / len(hums)

        if prev_temp is not None:
            if avg_temp > prev_temp:
                show_change("temp", True)
            elif avg_temp < prev_temp:
                show_change("temp", False)

        if prev_hum is not None:
            if avg_hum > prev_hum:
                show_change("hum", True)
            elif avg_hum < prev_hum:
                show_change("hum", False)

        prev_temp = avg_temp
        prev_hum = avg_hum
        last_update = now

    time.sleep(0.1)
