from gpiozero import RGBLED
import time

# Initialize RGB LED (R=17, G=27, B=22)
led = RGBLED(red=17, green=27, blue=22)

print("=== LED Blinking (1 second interval) ===")

try:
    while True:
        led.color = (1, 1, 1)  # ON (white)
        print("ON")
        time.sleep(1)

        led.color = (0, 0, 0)  # OFF
        print("OFF")
        time.sleep(1)

except KeyboardInterrupt:
    print("\n=== Stopped ===")

finally:
    led.close()