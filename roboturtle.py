from gpiozero import CamJamKitRobot
from turtle import Turtle
import time
import math	


WORLD_SCALE = 0.1


class RoboTurtle(Turtle):
	
	turn_speed = 1
	
	def __init__(self, *args, **kwargs):
		"""
		A Turtle that controls a CamJamRobot, using distance inputs.
		
		Args:
		  -robot (CamJamKitRobot): a robot that RoboTurtle should control. 
		      If None, RoboTurtle will make an instance itself.
		"""
		
		super(RoboTurtle, self).__init__(*args, **kwargs)
		self.robot = CamJamKitRobot()
		self.speed = 0.1
		self.scale = 0.1
	
	def _dist_to_time(self, move_fun, dist):
		"""converts a turtle movement distance to the robot's speed and timing commands""" 
		move_fun()
		time.sleep(dist * self.scale)
		self.robot.stop()
	
	def forward(self, dist):
		if dist < 0:
			self.backward(-dist)
		print('Moving forward {} units...'.format(dist))
		super(RoboTurtle, self).forward(dist)
		self._dist_to_time(self.robot.forward, dist)
		
	fd = forward
		
	def backward(self, dist):
		if dist < 0:
			self.forward(-dist)
		print('Moving backward {} units...'.format(dist))
		super(RoboTurtle, self).backward(dist)
		self._dist_to_time(self.robot.backward, dist)
		
	bk = backward
	back = backward
		
	def _degrees_to_time(self, turn_fun, degrees):
		turn_fun(self.turn_speed)
		time.sleep(3)  # TODO: Figure out relationship between speed, time, and degrees
		self.robot.stop()
		
	def left(self, degrees):
		if degrees < 0:
			return self.right(-degrees)
		print('Turning left {} degrees...')
		super(RoboTurtle, self).left(degrees)
		self._degrees_to_time(self.robot.left, degrees)
		
	lt = left
	
	def right(self, degrees):
		if degrees < 0:
			return self.left(-degrees)
		print('Turning right {} degrees...')
		super(RoboTurtle, self).left(degrees)
		self._degrees_to_time(self.robot.right, degrees)
		
	rt = right
	
	def goto(self, x, y=None):
		"""Goes to specified coordinates"""
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
		self.goto(self.scor(), y)
		
	def setheading(to_angle):
		"""Turn to a specific heading angle, in degrees"""
		to_turn = to_angle - self.heading()
		turn_fun = self.left if to_turn > 0 else self.right
		turn_fun(to_turn)

	seth = setheading
	
	def home(self):
		"""Go to the origin (0, 0)"""
		self.goto(0, 0)
		
	def circle(radius, extent=None, steps=None):
		raise NotImplementedError
		
	def undo(self):
		"""Undo the last action"""
		raise NotImplementedError
		
	
	def radians(self):
		"""Set the angle measurement units to radians"""
		raise NotImplementedError

	
	
	
if __name__ == '__main__':
	
	import turtle
	from time import sleep
	
	screen = turtle.Screen()
	
	turtle = RoboTurtle()
	
	for el in range(2):
		turtle.forward(100)
		sleep(2)
		turtle.left(90)
		sleep(2)
		turtle.backward(100)
		sleep(2)
		turtle.right(180)
		sleep(2)
	
