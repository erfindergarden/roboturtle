# roboturtle

The goal of this project is to take a python Turtle graphics script, change the turtle.Turtle class and change it to a RoboTurtle, and have your script control a robot that performs the on-screen actions while the turtle screen works.  This will hopefully provide a nice reward for students learning programming, and will increase engagement during the process!

This project is intended to be run on a Raspberry Pi, and requires the gpiozero package.
It can also be imported on a normal computer, however, which is useful for connecting remotely
to a Turtle via a Client-Server interface.

## Installation

Download the source code, and then use the setup.py file to install the roboturtle package:

```bash
cd roboturtle
python setup.py install
```

## Examples

### Creating a RobotTurtle

The roboturtle.RoboTurtle class is made to work exactly like python's turtle.Turtle class:

```python
from roboturtle import RoboTurtle

turtle = RoboTurtle()
turtle.forward(100) # Move forward 100 units
turtle.left(90)  # Turn left 90 degrees
turtle.backward(50)  # Move backward 100 units

```

### Creating a RoboTurtle on the Raspberry Pi and Hosting it on a Server

Note: this approach will work for any Python object!

On the Raspberry Pi:
```python
from roboturtle import RoboTurtle, EchoServer

turtle = RoboTurtle()

server = EchoServer(ip='my_ip_address', port=8000)
server.bind(turtle)  # This will start the event loop
```

### Connecting to a Remote EchoServer via an EchoClient

On your computer:
```python
from turtle import Turtle
from roboturtle import EchoClient

client = EchoClient(ip="sever's_ip_address", port=8000)

alex = turtle.Turtle()
client.bind(alex)  # This will modify the turtle so it automatically sends the commands on the client.

# Then, just give the turtle commands as normal!  The server will receive them all.
alex.forward(100)
alex.left(45)
```






