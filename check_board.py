# This code is to check if the onboard connections are working.

import time
import board
import neopixel

# Adafruit Bluefruit has 10 neopixels
num_pixels = 10
# Set the blink rate in seconds (on and off durations)
blink_rate = 0.1

# Initialize the NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=0.1, auto_write=False)

while True:
    # Turn all NeoPixels on with red color
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(blink_rate)

    # Turn all NeoPixels off
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(blink_rate)
