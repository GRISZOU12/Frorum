# this is a little server for the test of the client (the good server program is server and you can use it with main_pico.py on a raspberry pi pico)

import socket

HOST = "127.0.0.1"
PORT = 65432

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"{data} by {addr}")
                if data == b'ping':
                    to_send = b'ping'
                    conn.sendall(to_send)
                else:
                    to_send = b"bruh"
                    conn.sendall(to_send)
