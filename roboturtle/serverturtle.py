import socket
import threading
import json


def get_server_socket(ip=socket.gethostname(), port=80):
    """Returns a bound TCP Server socket."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(5)
    return sock



class Server(object):

    def __init__(self, sock, turtle):
        """
        A Server that continuously translates commands from a connected ClientTurtle, and implements them on a local
        RoboTurtle
        """

        self.server_sock = sock
        if not isinstance(self.server_sock, socket.socket):
            raise TypeError("Server.sock must be a bound socket.socket instance.")


        self.turtle = turtle
        (self.listening_sock, client_port) = self.server_sock.accept()
        print("Client Detected on port {}".format(client_port))

        self.thread = threading.Thread(target=self.listen_and_execute)
        self.thread.run()


    def listen_and_execute(self):

        while True:
            msg = self.listening_sock.recv(2 ** 9)
            print('Received message: {}'.format(msg))

            command = json.loads(msg.decode())
            getattr(self.turtle, command[0])(*command[1])


    @classmethod
    def from_address(cls, turtle, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((ip, port))
        sock.listen(5)
        return cls(sock, turtle)






