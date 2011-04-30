import game,objects,data
import pyglet

class Player(objects.Base):
	def __init__(self):
		self.hitbox = 'i dunno lol'
		self.i = 0
		objects.Base.__init__(self,data.fuckyeah,batch=game.batch)

	def tick(self):
		self.i += 1
		print self.i