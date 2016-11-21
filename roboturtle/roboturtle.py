import math
import time
from turtle import Vec2D, Turtle


class RoboTurtle(object):

    def __init__(self, robot=None, turn_speed=1.0, move_speed=1.0, time_offset=0., *args, **kwargs):
        """
        A turtle.Turtle for controlling a CamJamRobot, using distance inputs.
        """
        if robot:
            self.robot = robot
        else:
            import gpiozero
            self.robot = gpiozero.CamJamKitRobot() if not robot else robot

        self.turn_speed = turn_speed  # In full revolutions (360 degrees) per second
        self.move_speed = move_speed
        self.time_offset = time_offset
        self._heading_vec = Vec2D(1., 0.)
        self._current_coords = Vec2D(0., 0.)

    def __getattr__(self, item):
        if item in Turtle:
            raise NotImplementedError("{} not yet implemented in RoboTurtle class".format(item))
        else:
            raise AttributeError

    def forward(self, dist):
        """Move a robot forward some distance"""
        self.robot.forward(self.move_speed)
        self._current_coords += self._heading_vec * dist
        time.sleep(dist / self.move_speed) + self.time_offset
        self.robot.stop()

    def backward(self, dist):
        return self.forward(-dist)

    fd = forward
    bk = backward
    back = backward

    def left(self, degrees):
        self.robot.left(1.)  # To simplify the model, always turn at maximum speed.
        self._heading_vec = self._heading_vec.rotate(degrees)
        time.sleep(self.turn_speed / float(degrees)) + self.time_offset
        self.robot.stop()

    def right(self, degrees):
        return self.left(-degrees)

    lt = left
    rt = right

    def heading(self):
        angle = math.atan2(*self._heading_vec[::-1])
        angle = math.degrees(angle)
        return angle

    def xcor(self):
        return self._current_coords[0]

    def ycor(self):
        return self._current_coords[1]

    def distance(self, x, y):
        """Returns the robot's distance to coordinates (x, y)."""
        return abs(self._current_coords - Vec2D(x, y))

    def goto(self, x, y=None):
        """Goes to specified coordinates (x, y), leaving final heading unchanged."""
        if isinstance(y, type(None)):
            x, y = x
        x_old, y_old = self.heading()
        degrees_to_turn = math.degrees(math.atan2(y - y_old, x - x_old))
        self.left(degrees_to_turn)  # Turn toward coordinates
        self.forward(self.distance(x, y))  # Forward to coordinates
        self.right(degrees_to_turn)  # Turn back to original heading

    setpos = goto
    setposition = goto

    def setx(self, x):
        """Go to x position, leaving y position unchanged"""
        self.goto(x, self.ycor())

    def sety(self, y):
        """Go to y position, leaving x position unchanged"""
        self.goto(self.xcor(), y)

    def setheading(self, to_angle):
        """Turn to a specific heading angle, in degrees"""
        to_turn = to_angle - self.heading()
        self.left(to_turn)

    seth = setheading

    def home(self):
        """Go to the origin (0, 0)"""
        self.goto(0, 0)

    def circle(radius, *args, **kwargs):
        raise NotImplementedError

    def undo(self):
        """Undo the last action"""
        raise NotImplementedError

    def radians(self):
        """Set the angle measurement units to radians"""
        raise NotImplementedError