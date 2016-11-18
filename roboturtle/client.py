import types
import turtle
import json
import socket


def send_through_socket(sock):
    """A decorator that encodes all commands in json (function, args, kwargs) tuples, and sends it on a socket before calling the command."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            command = (func.__name__, args, kwargs)
            func_json = json.dumps(command)
            sock.send(func_json.encode())
            return func(*args, **kwargs)

        return wrapper
    return decorator


class EchoClient(object):

    def __init__(self, ip='localhost', port=8000):
        """
        A TCP client socket that can send serialized method calls on bound objects.

        Arguments:
            -ip (str): ip address of the server to connect to. Default: 'localhost'
            -port (int): port number of the server to connect to. Default: 8000
        """

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def bind(self, target):
        """Modifies a target object to send command packets."""

        for name in dir(target):

            # Filter out private methods and attributes
            if name[0] == '_':
                continue
            if not callable(getattr(target, name)):
                continue
            if name[:2] == 'on':
                continue

            # Apply decorator to method
            setattr(target, name, send_through_socket(self.sock)(getattr(target, name)))

