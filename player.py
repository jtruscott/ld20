import game,objects,data
import pygame
from pygame.locals import *
import funcs as F

import logging
log = logging.getLogger('player')

class BodyPart:
	def __init__(self,component,**kw):
		self.component = component
		for k,v in kw.items():
			setattr(self,k,v)
	
class Player(objects.Base):
	stack_order = ['body','tail','horn','dorsal']
	stats = {
		'armor':0,		'damage':0,
		'maxhp':0,		'thorns':0,
		'horn_regen':0,	'body_regen':0,
		'maxspeed':0,	'turning':0,
		}
	def __init__(self):
		self.hitbox = 'i dunno lol'
		objects.Base.__init__(self,'player',game.config.width / 2,game.config.height / 2)
		self.parts_table = {
				'body': [
					BodyPart(data.player.body, maxhp=20.0, armor=0, body_regen=0.5)
					],
				'horn': [
					BodyPart(data.player.horn_a, damage=5, horn_regen = 1)
					],
				'tail': [
					BodyPart(data.player.tail_a, maxspeed=10, turning=100)
					],
				'dorsal': [
					BodyPart(None),
					BodyPart(data.player.dorsal_b, maxspeed=2, maxhp=2)
					],
				}
		self.parts = {}
		for part,options in self.parts_table.items():
			self.parts[part] = options[0]
		
		self.build_narwhal()
				
	def build_narwhal(self):
		self.update_stats()
		
		W = 24+48+24
		H = 48+24
		narwhal = pygame.Surface((W,H))
		narwhal.convert()
		narwhal.fill((255,0,110))
		#blit the components
		for part in self.stack_order:
			component = self.parts[part].component
			if component is None: continue
			dest = component.surf.get_rect()
			dest.centerx = W/2 + component.x
			dest.centery = H/2 + component.y
			narwhal.blit(component.surf,dest)
			
		narwhal.set_colorkey(narwhal.get_at((0,0)))
		self.narwhal = narwhal
	
	def update_stats(self):
		for stat in self.stats.keys():
			self.stats[stat] = sum([getattr(part,stat,0) for part in self.parts.values()])
		log.debug(self.stats)
		
	def rect_update(self):
		self.rect.centerx = min(self.x,game.config.width / 2)
		self.rect.centery = self.y
		
	def update_image(self):
		wret = pygame.transform.rotate(self.narwhal,0)
		self.image = wret
		self.rect = wret.get_rect()
		self.rect_update()
		
	def update(self):
		self.update_image()
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.x -= 1
		if keys[K_RIGHT]:
			self.x += 1
