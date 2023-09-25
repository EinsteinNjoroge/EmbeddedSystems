import machine
import utime

# Define GPIO pins
trig_pin = machine.Pin(26, machine.Pin.OUT)  # GPIO pin for TRIG
echo_pin = machine.Pin(27, machine.Pin.IN)  # GPIO pin for ECHO

# Function to measure distance
def measure_distance():
    # Send a 10us trigger pulse to start the measurement
    trig_pin.value(1)
    utime.sleep_us(10)
    trig_pin.value(0)

    # Wait for the ECHO pin to go high (start of echo pulse)
    while echo_pin.value() == 0:
        pass
    start_time = utime.ticks_us()

    # Wait for the ECHO pin to go low (end of echo pulse)
    while echo_pin.value() == 1:
        pass
    end_time = utime.ticks_us()

    # Calculate the duration of the pulse (in microseconds)
    pulse_duration = utime.ticks_diff(end_time, start_time)

    # Convert the duration to distance (in centimeters)
    # Speed of sound is approximately 343 meters per second
    # Distance = (duration * speed of sound) / 2
    distance_cm = (pulse_duration * 343) / (2 * 10000)  # Convert to centimeters

    return distance_cm

# Main loop
while True:
    distance = measure_distance()
    print("Distance:", distance, "cm")
    utime.sleep(1)  # Sleep for 1 second before the next measurement