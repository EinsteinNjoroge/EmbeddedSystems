# This is a sample Python script.
from passive_infrared_sensor import detect_motion
from distance import measure_distance
from machine import Pin
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


while True:
    distance = measure_distance()
    motion_detected = detect_motion()
    print("motion detected ==> ", motion_detected)
    output = Pin(17, Pin.OUT)
    if distance <= 100 & motion_detected:
        print("Distance:", distance, "cm")
        sleep_time = distance / 100
        output.on()
        time.sleep(sleep_time)
        output.off()

    time.sleep(0.1)
