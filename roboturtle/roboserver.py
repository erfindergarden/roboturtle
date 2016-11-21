from roboturtle import EchoServer, RoboTurtle
import turtle
import click

@click.command()
@click.option('--ip', type=str, default='localhost', help='IP address of roboserver')
@click.option('--port', type=int, default=8000, help='port number of roboserver')
@click.option('--turn_speed', type=float, default=1.0, help='Turn speed (full revolutions per second) of robot')
@click.option('--move_speed', type=float, default=1.0, help='Movement speed of robot')
@click.option('--time_offset', type=float, default=0., help='Offset lag time, in seconds (negative means subtract for lag time, to compensate)')
def start_roboserver(ip, port, turn_speed, move_speed, time_offset):
    """Start a roboturtle EchoServer and bind it to a newly-created RoboTurtle (requires gpiozero to be installed)."""
    server = EchoServer(ip=ip, port=port)
    turtle = RoboTurtle(turn_speed=turn_speed, move_speed=move_speed, time_offset=time_offset)
    while True:
        try:
            server.bind(turtle)
        except NotImplementedError:
            pass


@click.command()
@click.option('--ip', type=str, default='localhost', help='IP address of roboserver.')
@click.option('--port', type=int, default=8000, help='Port number of roboserver to connect to.')
def start_turtleserver(ip, port):
    server = EchoServer(ip=ip, port=port)
    alex = turtle.Turtle(shape='turtle')
    while True:
        server.bind(alex)