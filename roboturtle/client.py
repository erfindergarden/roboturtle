import json
import socket


def send_through_socket(sock):
    """
    A decorator that encodes all commands in json (function, args, kwargs) tuples, and echos it on a socket.
    The command's format will be semt as (function_name <str>, *args <tuple>, **kwargs <dict>)
    """
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
        socket_sender = send_through_socket(self.sock)
        targ_methods = [name for name in dir(target) if not callable(getattr(target, name)) or name[:2] in ['_', 'on']]
        for name in targ_methods:
            setattr(target, name, socket_sender(getattr(target, name)))
