import socket
import sys
import time

from bme280 import bme280

I2C_CH = 1
BME280_ADDR = 0x76

ECHOMAX = 256
SLEEP_TIME = 0.001

def die_with_error(message):
    print(message, file=sys.stderr)
    sys.exit(1)

def read_sensor_string():
    data = bme280.read_all()
    return (f"Temperature:{round(data.temperature, 2)},"
            f"Humidity:{round(data.humidity, 2)},"
            f"Pressure:{round(data.pressure, 2)}")

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"Usage: {sys.argv[0]} <Server IP> [<Echo Port>]", file=sys.stderr)
        sys.exit(1)

    serv_ip = sys.argv[1]
    echo_serv_port = int(sys.argv[2]) if len(sys.argv) == 3 else 7

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except OSError:
        die_with_error("socket() failed")

    bme280.full_setup(I2C_CH, BME280_ADDR)

    dest = (serv_ip, echo_serv_port)

    num = 0

    while True:
        echo_string = read_sensor_string()
        echo_bytes = echo_string.encode()

        if len(echo_bytes) > ECHOMAX:
            die_with_error("Echo word too long")

        sent = sock.sendto(echo_bytes, dest)
        if sent != len(echo_bytes):
            die_with_error("sendto() sent a different number of bytes than expected")
        print(f"Sent [{num}]: {echo_string}")

        sent = sock.sendto(echo_bytes, dest)
        if sent != len(echo_bytes):
            die_with_error("sendto() sent a different number of bytes than expected")
        print(f"Sent [{num}]: {echo_string}")

        num += 1
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
