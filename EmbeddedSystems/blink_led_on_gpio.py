import math
from machine import Pin
import time

# # Stream blink led bulbs
# onboard_led = Pin(25, Pin.OUT)
# onboard_led.on()
#
# red = Pin(2, Pin.OUT)
# yellow = Pin(4, Pin.OUT)
# green = Pin(6, Pin.OUT)
#
# sleep_time = 4
# transition_time = 1
# traffic_lights = [red, green]
#
#
# def transition():
#     yellow.on()
#     time.sleep(transition_time)
#     yellow.off()
#
#
# while True:
#     for bulb in traffic_lights:
#         bulb.on()
#         time.sleep(sleep_time)
#         transition()
#         bulb.off()

red_pins = [19, 20, 21, 22, 26, 27, 28]
yellow_pins = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
green_pins = [ 0, 1, 2, 3, 4, 5, 6, 7, 8]

red_leds = []
green_leds = []
yellow_leds = []

for pin in red_pins:
    led = Pin(pin, Pin.OUT)
    red_leds.append(led)

for pin in yellow_pins:
    led = Pin(pin, Pin.OUT)
    yellow_leds.append(led)

for pin in green_pins:
    led = Pin(pin, Pin.OUT)
    green_leds.append(led)

all_leds = green_leds + yellow_leds + red_leds


def light_all():
    for led in all_leds:
        led.on()


def dim_all():
    for led in all_leds:
        led.off()


# Light all leds in a sequence
def sequence_one():
    for led in all_leds:
        led.on()
        time.sleep(0.1)
        led.off()


# def sequence_two():
#     sequence = [green_leds, yellow_leds, red_leds]
#     for i in sequence:
#         for led in i:
#             led.on()
#             time.sleep(0.15)
#             led.off()


# light
def sequence_three():
    half = math.floor(len(all_leds) / 2)
    for i in range(0, half):
        led = all_leds[i]
        # led_11 = all_leds[i + 1]
        # led_12 = all_leds[i + 2]

        led_2 = all_leds[i + half]
        # led_21 = all_leds[i + half + 1]
        # led_22 = all_leds[i + half + 2]

        led.on()
        # led_11.on()
        # led_12.on()

        led_2.on()
        # led_21.on()
        # led_22.on()

        time.sleep(0.1)
        # led.off()
        # led_11.off()
        # led_12.off()

        # led_2.off()
        # led_21.off()
        # led_22.off()
        dim_all()


# dim_all()
# light_all()
while True:
    sequence_three()
    # sequence_one()
# for led in green_leds:
#     led.off()
#
# for led in yellow_leds:
#     led.off()
#
# for led in red_leds:
#     led.off()
