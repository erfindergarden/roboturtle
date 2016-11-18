import socket
import json


class EchoServer(object):

    def __init__(self, ip='localhost', port=8000):

        # Create and Bind Server Socket to Address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.sock.listen(5)

        self.client = None

    def wait_for_client_connection(self):

        print("Waiting for a client to connect...")
        assert not self.client, "New Client trying to connect when one is already connected."

        self.client, port = self.sock.accept()
        print("New Client connected on port {}.".format(port))

    def recv_json(self, nbytes=2**10):

        msg = self.client.recv(nbytes)
        print('Received message: {}'.format(msg))

        if not msg:
            return msg
        else:
            return json.loads(msg.decode())

    def bind(self, target):
        """
        Binds a target object and starts the event loop, copying all received
        commands and calling them on the target object.

        Note: This is a blocking operation.
        """

        while True:
            if not self.client:
                self.wait_for_client_connection()

            command = self.recv_json()
            if not command:
                print("Empty message received. Deleting client and waiting for new connection...")
                self.client = None
                continue

            # Execute JSON command on target
            getattr(target, command[0])(*command[1])







