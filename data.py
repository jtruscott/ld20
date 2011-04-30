import pygame,os,os.path
from pygame.locals import *
from collections import namedtuple
import logging

log = logging.getLogger("data")
Comp = namedtuple('Comp',('surf','x','y'))
images = {
	'player': [
		('horn_a',32,0),
		('tail_a',-40,0),
		('dorsal_b',0,-24),
		('body',0,0),
		('blank',0,0)
		],
	'bubble': ['bubble%s' % i for i in range(2)]
	
	}

def load_png(path):
	""" Load image and return image object"""
	log.debug("Loading png %s",path)
	if isinstance(path,basestring):
		name = path
		path = os.path.join(os.getcwd(),"images","%s.png" % path)
	else:
		name = path[-1]
		path[-1] = "%s.png" % path[-1]
		path = os.path.join(os.getcwd(),*path)
	try:
		image = pygame.image.load(path)
		if image.get_alpha() is None or True:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error, message:
        	print 'Cannot load image:', name
        	raise SystemExit, message
	hw = pygame.Surface((image.get_rect().width,image.get_rect().height),HWSURFACE|HWPALETTE|RLEACCEL|SRCALPHA)
	hw.set_colorkey(image.get_at((0,0)))
	hw.blit(image,image.get_rect())
	return hw

def init():
	import data #yeah.
	
	for key,files in images.items():
		if isinstance(files,list):
			#multiple files
			if isinstance(files[0],basestring):
				#just a list
				surfs = []
				for file in files:
					surfs.append(load_png(file))
			else:
				#oh god composite
				surfs = {}
				for (file,x,y) in files:
					surfs[file] = Comp(load_png(file),x,y)
				surfs = namedtuple(key,[f for f,x,y in files])(**surfs)
		else:
			surfs = load_png(files)
		log.debug("%s: %s",key,surfs)
		#this isnt fucking magic at all i swear
		setattr(data,key,surfs)