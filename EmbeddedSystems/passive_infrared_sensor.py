from machine import Pin
import time

pin = Pin(18, Pin.IN, Pin.PULL_DOWN)

print('Starting up the PIR Module')


def detect_motion():
    return pin.value() == 1


# while True:
#     if detect_motion():
#         print('Motion Detected ')
#     time.sleep(1)

