import lgpio
import time
SERVO_PIN = 24
degree = 30
MIN_DEG = 0
MAX_DEG = 180
MIN_PULSE = 500
MAX_PULSE = 2400

a = float(MAX_PULSE - MIN_PULSE) / float(MAX_DEG - MIN_DEG)
b = MIN_PULSE
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, SERVO_PIN)
while True:
    degree = (degree + 60) % 180
    pulse = int(a * float(degree) + b)
    lgpio.tx_servo(h, SERVO_PIN, pulse)
    time.sleep(1)