from gpiozero import RGBLED, Button
from signal import pause

# RGB LED pin configuration (Red, Green, Blue)
# *If the colors appear incorrectly, swap the pin numbers below.
led = RGBLED(red=17, green=27, blue=22)
button = Button(25)

# List of color values (R, G, B intensity from 0.0 to 1.0)
colors = [
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (1, 0, 1),  # Purple
    (1, 1, 0),  # Yellow
    (0, 1, 1),  # Cyan
    (0, 0, 0)   # Off
]

color_index = 0

def change_color():
    global color_index
    # Set current color
    led.color = colors[color_index]
    # Advance to the next color
    color_index = (color_index + 1) % len(colors)

# Change color when the button is pressed
button.when_pressed = change_color

pause()
