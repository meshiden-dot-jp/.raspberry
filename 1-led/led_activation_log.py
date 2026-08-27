from gpiozero import RGBLED, Button
import time

# Initialize RGB LED (R=17, G=27, B=22) and Button (25)
# RGBLED is a class provided by the gpiozero library
led = RGBLED(red=17, green=27, blue=22)
button = Button(25, bounce_time=0.05)  # Added debounce protection

MEASURE_TIME = 15.0  # Measurement duration in seconds

print("=== Lighting Time Recording Fot 15 Seconds ===")

toggle_count = 0        # Number of times turned on
total_on_time = 0.0     # Total lighting time in seconds
is_lit = False          # Current state (False: OFF, True: ON)
light_start_time = 0.0  # Timestamp when turned on

start_time = time.time()

while (time.time() - start_time) < MEASURE_TIME:
    # Detect when the button is pressed
    if button.is_pressed:
        if not is_lit:
            # [OFF -> ON] If currently OFF and button is pressed, turn ON
            led.color = (1, 1, 1)  # Turn on white LED
            is_lit = True
            light_start_time = time.time()  # Record start time
            toggle_count += 1
            print(f"[{toggle_count}] Turned ON")
        else:
            # [ON -> OFF]
            led.color = (0, 0, 0)  # Turn OFF
            is_lit = False
            on_duration = time.time() - light_start_time  # Calculate current lighting duration
            total_on_time += on_duration
            print(f"Turned OFF (Current duration: {on_duration:.2f}s)")

        # Prevent false triggering from rapid button spamming
        time.sleep(0.2)

# If still lit when the loop finishes, add remaining time and turn OFF
if is_lit:
    on_duration = time.time() - light_start_time
    print(f"Until time runs out (Current duration: {on_duration:.2f}s)")
    total_on_time += on_duration
    led.color = (0, 0, 0)

print("\n=== Time is up ===")
print(f"Toggle count: {toggle_count} times")
print(f"Total lighting time: {total_on_time:.2f} seconds")

led.close()