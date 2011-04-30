import pygame,rabbyt,sys
import game,data
import logging
logging.basicConfig(level=5,stream=sys.stdout,format='%(levelname)s: %(name)s - %(message)s')
log = logging.getLogger("core")
def init():
	log.info("Setting up")
	pygame.init()
	game.window = pygame.display.set_mode(game.config.size,game.config.screenargs)
	rabbyt.set_viewport(game.config.size)
	rabbyt.set_default_attribs()
	
	
if __name__ == '__main__':
	init()
	data.init()
	game.init()
	game.loop()