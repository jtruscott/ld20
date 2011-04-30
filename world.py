import pygame
import pymunk as pm
import game,objects
from random import *

class World:
	def __init__(self):
		self.w,self.h = game.config.size
		self.bubbletimer = 1
	def update(self):
		self.bubbletimer -= 1
		if self.bubbletimer == 0:
			self.bubbletimer = 10
			objects.Bubble(game.player.x + randint(-self.w,self.w),self.h)
		
		
def Background():
	background = pygame.Surface(game.config.size)
	background = background.convert()
	background.fill((180,215,220))
	return background