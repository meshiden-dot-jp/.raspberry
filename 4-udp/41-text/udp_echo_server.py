import socket
import sys

ECHOMAX = 255

def die_with_error(message):
    print(message, file=sys.stderr)
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <UDP SERVER PORT>", file=sys.stderr)
        sys.exit(1)

    echo_serv_port = int(sys.argv[1])

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except OSError:
        die_with_error("socket() failed")

    try:
        sock.bind(("", echo_serv_port))
    except OSError:
        die_with_error("bind() failed")

    print(f"Server listens on port {echo_serv_port}")

    num = 0

    while True:
        try:
            data, clnt_addr = sock.recvfrom(ECHOMAX)
        except OSError:
            die_with_error("recvfrom() failed")

        print(f"[{num}] message: {data.decode(errors='replace')} from {clnt_addr[0]}")

        num += 1

if __name__ == "__main__":
    main()
