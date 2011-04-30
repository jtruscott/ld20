import pyglet
import pymunk as pm
import game

class Base(pyglet.sprite.Sprite):
	def __init__(self,*args,**kwargs):
		pyglet.sprite.Sprite.__init__(self,*args,**kwargs)
		game.objects.append(self)
		
		