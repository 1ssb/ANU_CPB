import time
from adafruit_circuitplayground import cp

# Define the activity as a list of lists: [name, RGB tuple, tone frequency]
activity = [
    ["Red", (255, 0, 0), 262],  # C4
    ["Orange", (255, 127, 0), 294],  # D4
    ["Yellow", (255, 255, 0), 330],  # E4
    ["Green", (0, 255, 0), 349],  # F4
    ["Blue", (0, 0, 255), 392],  # G4
    ["Indigo", (75, 0, 130), 440],  # A4
    ["Violet", (148, 0, 211), 494],  # B4
    ["Pink", (255, 192, 203), 523],  # C5
]

num_pixels = 10  # Number of NeoPixels on the CPB
cp.pixels.brightness = 0.3  # Set initial brightness
color_index = 0  # Starting index for color rotation


def update_pixels(rgb_color):
    for i in range(num_pixels):
        cp.pixels[i] = rgb_color


while True:
    name, rgb, tone = activity[color_index]
    update_pixels(rgb)
    print(f"Color: {name}")
    cp.play_tone(tone, 0.5)  # Play tone for 0.5 seconds
    time.sleep(0.5)  # Wait before next color
    color_index = (color_index + 1) % len(activity)  # Move to next color
