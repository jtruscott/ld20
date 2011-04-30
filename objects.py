import pyglet
import pymunk as pm
import game

class Cursor:
	def __init__(self):
		self.body = pm.Body(pm.inf, pm.inf)
		self.shape = pm.Circle(self.body, 3, Vec2d(0,0))
		self.shape.coltype = game.ColType.cursor
		game.space.add(self.shape)
