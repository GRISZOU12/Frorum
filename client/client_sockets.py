import socket

HOST = "127.0.0.1"
PORT = 65432


def ping():
    try:
        to_send = b'pin'
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(to_send)
            response = s.recv(1024)
            if response == to_send:
                return True
            else:
                return False
    except WindowsError:
        return False
