import pygame
import rabbyt
import config
import world


def lib_init():
	pygame.init()
	pygame.display.set_mode(config.size, pygame.OPENGL | pygame.DOUBLEBUF)
	rabbyt.set_viewport(config.size)
	rabbyt.set_default_attribs()

	
lib_init()

