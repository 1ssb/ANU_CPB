import time
import random
import adafruit_circuitplayground.express as cpx

# Adjust this value based on your testing.
# The CPX ambient light sensor reading can vary; experiment to pick the best threshold.
LIGHT_THRESHOLD = 300


def wheel(pos):
    """
    Generate rainbow colors across 0-255 positions.
    This helper function returns an (R, G, B) tuple for a given position.
    """
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)


def rainbow_cycle(wait):
    """
    Animate a rainbow cycle on the onboard NeoPixels.
    It will check the ambient light during the loop and exit early if conditions change.
    """
    num_pixels = len(cpx.pixels)
    for j in range(256):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels + j) & 255
            cpx.pixels[i] = wheel(pixel_index)
        cpx.pixels.show()
        time.sleep(wait)
        # If it suddenly becomes bright, break out of the rainbow cycle.
        if cpx.light > LIGHT_THRESHOLD:
            break


def blue_sparkle(wait):
    """
    Display a blue sparkle effect by randomly lighting pixels in blue.
    This effect is intended for bright conditions.
    """
    num_pixels = len(cpx.pixels)
    cpx.pixels.fill((0, 0, 0))
    for i in range(num_pixels):
        # About 30% chance to light a pixel.
        if random.random() > 0.7:
            cpx.pixels[i] = (0, 0, 255)
    cpx.pixels.show()
    time.sleep(wait)


while True:
    # Read the ambient light sensor value.
    light_val = cpx.light
    print("Ambient Light:", light_val)

    # Choose the animation based on the current light level.
    if light_val < LIGHT_THRESHOLD:
        # Dark: run the rainbow cycle.
        rainbow_cycle(0.03)
    else:
        # Bright: run the blue sparkle effect.
        blue_sparkle(0.1)
