import time
from adafruit_circuitplayground import cp

# Configuration
cp.pixels.brightness = 0.1

# Global Thresholds
LIGHT_THRESHOLD = 100
NUM_PIXELS = 10
SHAKE_THRESHOLD = 20  # Adjust sensitivity: lower is more sensitive

while True:
    # Read light sensor value
    light_level = cp.light

    # Update NeoPixels based on light level
    if light_level > LIGHT_THRESHOLD:
        for i in range(NUM_PIXELS):
            cp.pixels[i] = (0, 255, 0)  # Green
        cp.pixels.show()
        time.sleep(1)
    else:
        for i in range(NUM_PIXELS):
            cp.pixels[i] = (0, 0, 0)  # Off
        cp.pixels.show()

    # Check for shake event
    if cp.shake(shake_threshold=SHAKE_THRESHOLD):
        print("CPB shaking!")
        cp.play_tone(440, 1)  # A4 note for 1 second

    # Debugging output
    x, y, z = cp.acceleration
    print(f"Light Level: {light_level}, Acceleration: x={x:.2f}, y={y:.2f}, z={z:.2f}")

    time.sleep(0.1)
