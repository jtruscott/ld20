import config
import pygame

class World:
	def __init__(self):
		self.viewport = pygame.Rect((0,0),config.size)
		
world = World()