import types
import turtle
import json
import socket


def send_through_socket(sock):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_dict = {func.__name__: [args, kwargs]}
            func_json = json.dumps(func_dict)
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

            # Apply decorator to method
            setattr(self, name, send_through_socket(sock)(getattr(self, name)))




