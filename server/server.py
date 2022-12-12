import socket
import time

class Server:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 65432
        # here is the basics error that you can encounter with a bad usage of the server
        self.ERROR_InvalidRequest_UNDEFINED = "Error : InvalidRequest-UNDEFINED"
        self.ERROR_InvalidRequest_ILLEGAL = "Error : InvalidRequest-ILLEGAL"
        # this is the var that is sended to client (by default it's an error)
        self.to_send = self.ERROR_InvalidRequest_UNDEFINED.encode()
        # this is the variable that's used when the server is pinged
        self.pinged = b'ping'

    def work(self):
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.HOST, self.PORT))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        if data == self.pinged:
                            print(f"|Server pinged by {addr}")
                            with open("./datas/ping_requests", "a") as new_ping_request:
                                new_ping_request.write(f"\nPing request : [{data}] received from {addr} at {time.time()}\n")
                            self.to_send = self.pinged
                            conn.sendall(self.to_send)
                        else:
                            print(f"|Illegal request received from {addr}")
                            with open("./datas/illegal_requests", "a") as new_illegal_request:
                                new_illegal_request.write(f"\nNew illegal request : [{self.ERROR_InvalidRequest_ILLEGAL}] received from {addr} at {time.time()}\n")
                            self.to_send = self.ERROR_InvalidRequest_ILLEGAL
                            conn.sendall(self.to_send.encode())
