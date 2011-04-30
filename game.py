#i'm going to put all my "static" stuff here like it's global
import pymunk as pm
import world as w
import player as p
import objects as o
import config
import pygame
from pygame.locals import *
import logging

objects = []
class ColType:
	player,terrain = range(900,902)
 
log = logging.getLogger("game")
def init():
	#Build all the objects we use
	log.info("Building objects")
	global groups,background,player,space,fps,objects,clock,loop,running
	background = w.Background()
	groups = {
		'worldfx': pygame.sprite.RenderUpdates(),
		'world': pygame.sprite.RenderUpdates(),
		'player': pygame.sprite.RenderUpdates(),
		'effects': pygame.sprite.RenderUpdates(),
		'foes': pygame.sprite.RenderUpdates()
		}
	grouplist = (groups['worldfx'],groups['world'],groups['player'],groups['foes'],groups['effects'])
	world = w.World()
	player = p.Player()
	space = pm.Space()
	clock = pygame.time.Clock()
	running = True
	
	def loop():
		log.info("Entering game loop")
		while running:
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					return
			window.blit(background,background.get_rect())
			world.update()
			for group in grouplist:
				group.update()
			for group in grouplist:
				group.draw(window)
			#draw
			pygame.display.flip()
			clock.tick(config.fps)
			pygame.display.set_caption("Narwhal Jousting! (%.1ffps)" % clock.get_fps())
