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
            func(*args, **kwargs)

        return wrapper
    return decorator



class ClientTurtle(turtle.Turtle):

    def __init__(self, sock, *args, **kwargs):
        """A Wrapper for the turtle.Turtle class, which sends a JSON packet through a client socket when"""

        if not isinstance(sock, socket.socket):
            raise TypeError

        super(ClientTurtle, self).__init__(*args, **kwargs)

        for name in dir(ClientTurtle):

            # Filter out private methods and attributes
            if name[0] == '_':
                continue
            if type(getattr(ClientTurtle, name)) != types.FunctionType:
                continue
            if name[:2] == 'on':
                continue

            # Apply decorator to method
            setattr(self, name, send_through_socket(sock)(getattr(self, name)))

    @classmethod
    def from_address(cls, ip, port):
        """Builds a socket, connects it, and returns the ClientTurtle directly."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        return cls(sock)
