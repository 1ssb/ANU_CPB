from adafruit_circuitplayground import cp
import time

while True:
    if cp.button_a:
        print("Button A pressed!")
    if cp.button_b:
        print("Button B pressed!")
    time.sleep(0.2)
