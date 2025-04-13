import time
from adafruit_circuitplayground import cp

# Global debounce delay
DEBOUNCE_DELAY = 0.05  # Adjust this value for faster or slower debounce

# Define the activity list as a list of tuples:
# (Index, Color Name, RGB Tuple, Tone Frequency)
activity = [
    (0, "Red", (255, 0, 0), 262),  # C4
    (1, "Orange", (255, 127, 0), 294),  # D4
    (2, "Yellow", (255, 255, 0), 330),  # E4
    (3, "Green", (0, 255, 0), 349),  # F4
    (4, "Blue", (0, 0, 255), 392),  # G4
    (5, "Indigo", (75, 0, 130), 440),  # A4
    (6, "Violet", (148, 0, 211), 494),  # B4
    (7, "Pink", (255, 192, 203), 523),  # C5
]

num_pixels = 10  # Number of NeoPixels on the CPB
cp.pixels.brightness = 0.3  # Set initial brightness
color_index = 0  # Starting index for color rotation
direction = 1  # 1 for clockwise, -1 for counter-clockwise

print("Press Button A to toggle rotation direction.")
print("Press Button B to reverse the color sequence.")


def update_pixels(rgb_color, direction):
    if direction == 1:
        for i in range(num_pixels):
            cp.pixels[i] = rgb_color
            time.sleep(0.1)
    else:
        for i in reversed(range(num_pixels)):
            cp.pixels[i] = rgb_color
            time.sleep(0.1)
    cp.pixels.show()
    time.sleep(0.2)


while True:
    idx, name, rgb, tone = activity[color_index]
    update_pixels(rgb, direction)
    print(f"Color index and name: {idx}, {name}")
    cp.play_tone(tone, 0.5)  # Play tone for 0.5 seconds
    time.sleep(0.5)  # Wait before next color

    # Check for Button A press to toggle direction
    if cp.button_a:
        direction *= -1  # Toggle between 1 and -1
        print("Changing Direction of Light!")
        time.sleep(DEBOUNCE_DELAY)  # Debounce delay

    # Check for Button B press to reverse the activity list
    if cp.button_b:
        activity.reverse()
        print("Color sequence reversed.")
        time.sleep(DEBOUNCE_DELAY)  # Debounce delay

    # Update color index based on direction
    color_index = (color_index + direction) % len(activity)
