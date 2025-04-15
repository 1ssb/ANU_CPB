# FSMs are a very important logical modelling in discrete systems. Some of you will use it without knowing that you are inherently using it.
# I would like you to go through this in detail: https://www.freecodecamp.org/news/state-machines-basics-of-computer-science-d42855debc66/

import time
from adafruit_circuitplayground import cp

# Define states
STATE_IDLE = 0
STATE_RED = 1
STATE_BLUE = 2
STATE_PAUSED = 3

state = STATE_IDLE
blink = False
last_blink_time = time.monotonic()
blink_interval = 0.5  # seconds

print("Starting FSM. Initial State: Idle (White)")

while True:
    # Button A pressed: advance state
    if cp.button_a:
        state = (state + 1) % 4  # Cycle through 0 to 3
        print("Button A pressed. Advancing to next state.")
        time.sleep(0.2)  # Debounce delay

    # Button B pressed: reset to Idle
    if cp.button_b:
        state = STATE_IDLE
        print("Button B pressed. Resetting to Idle state.")
        time.sleep(0.2)  # Debounce delay

    current_time = time.monotonic()

    if state == STATE_IDLE:
        cp.pixels.fill((255, 255, 255))  # White
        blink = False
    elif state == STATE_RED:
        if current_time - last_blink_time >= blink_interval:
            blink = not blink
            last_blink_time = current_time
        cp.pixels.fill((255, 0, 0) if blink else (0, 0, 0))  # Red blinking
    elif state == STATE_BLUE:
        if current_time - last_blink_time >= blink_interval:
            blink = not blink
            last_blink_time = current_time
        cp.pixels.fill((0, 0, 255) if blink else (0, 0, 0))  # Blue blinking
    elif state == STATE_PAUSED:
        cp.pixels.fill((0, 255, 0))  # Green
        blink = False

    time.sleep(0.05)
