import pyglet,rabbyt,sys
import game

from pyglet.window import key

def init():
	game.window = pyglet.window.Window(height=game.config.height,width=game.config.width,caption=game.title)
	rabbyt.set_viewport(game.config.size)
	rabbyt.set_default_attribs()
	game.init()
	
def global_setup():
	w,fps = game.window,game.fps
	@w.event
	def on_key_press(symbol,modifiers):
		print key.symbol_string(symbol)
		if symbol == key.C and modifiers & key.LCTRL:
			sys.exit()
	@w.event
	def on_draw():
		w.clear()
		game.batch.draw()
		fps.draw()
	
	
if __name__ == '__main__':
	init()
	global_setup()
	pyglet.app.run()