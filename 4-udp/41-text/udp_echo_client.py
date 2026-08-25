import socket
import sys
import time

ECHOMAX = 256
SLEEP_TIME = 0.001

def die_with_error(message):
    print(message, file=sys.stderr)
    sys.exit(1)

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(f"Usage: {sys.argv[0]} <Server IP> <Echo Word> [<Echo Port>]", file=sys.stderr)
        sys.exit(1)

    serv_ip = sys.argv[1]
    echo_string = sys.argv[2]

    if len(echo_string) > ECHOMAX:
        die_with_error("Echo word too long")

    echo_serv_port = int(sys.argv[3]) if len(sys.argv) == 4 else 7

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except OSError:
        die_with_error("socket() failed")

    echo_bytes = echo_string.encode()
    dest = (serv_ip, echo_serv_port)

    num = 0

    while True:
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

    # 元のコードと同様、無限ループの後には到達しない
    from_size = None
    data, from_addr = sock.recvfrom(ECHOMAX)
    if len(data) != len(echo_bytes):
        die_with_error("recvfrom() failed")

    if from_addr[0] != serv_ip:
        print("Error: received a packet from unknown source.", file=sys.stderr)
        sys.exit(1)

    print(f"Received: {data.decode(errors='replace')}")

    sock.close()

if __name__ == "__main__":
    main()
