import pygame
import pymunk as pm
import game,data
import funcs as F
from random import *

class Base(pygame.sprite.Sprite):
	def __init__(self,group,x,y,*args,**kwargs):
		pygame.sprite.Sprite.__init__(self)
		game.groups[group].add(self)
		self.x = x
		self.y = y
		
	def rect_update(self):
		F.coord_to_viewport(self.rect,self.x,self.y)
	def update(self):
		self.rect_update()
	
class Animated(Base):
	
	def __init__(self,*args):
		Base.__init__(self,*args)
		self.tick = 1
		self.frame = -1
		self.anim_update()
		
	def anim_update(self):
		self.tick -= 1
		if self.tick == 0:
			self.tick = self.delay
			self.frame = (self.frame + 1) % len(self.images)
			self.image = self.images[self.frame]
			self.rect = self.image.get_rect()
			
	def update(self):
		self.anim_update()
		self.rect_update()
		
class Bubble(Animated):
	delay = 5
	def __init__(self,x,y):
		self.images = data.bubble
		Animated.__init__(self,'worldfx',x,y)
		
	def update(self):
		self.y -= 3 + randint(-1,1)
		self.x += randint(-1,1)
		if self.y < -self.rect.height:
			self.kill()
		Animated.update(self)
		