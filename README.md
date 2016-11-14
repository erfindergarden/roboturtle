# roboturtle

The goal of this project is to take a python Turtle graphics script, change the turtle.Turtle class and change it to a RoboTurtle, and have your script control a robot that performs the on-screen actions while the turtle screen works.  This will hopefully provide a nice reward for students learning programming, and will increase engagement during the process!

This project must be run on a Raspberry Pi, and requires the gpiozero package.

## Usage Example

The roboturtle.RoboTurtle class is made to work exactly like python's turtle.Turtle class::

```python
from roboturtle import RoboTurtle

turtle = RoboTurtle()
turtle.forward(100) # Move forward 100 units
turtle.left(90)  # Turn left 90 degrees
turtle.backward(50)  # Move backward 100 units

```

