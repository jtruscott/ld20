#i'm going to put all my "static" stuff here like it's global
import pymunk as pm
import world as w
import player as p
import objects as o
import config
import pyglet

title = "Narwhal Jousting!"
class ColType:
	player,terrain = range(900,902)
 
def init():
	#Build all the objects we use
	global world,player,space,fps
	world = w.World()
	player = p.Player()
	space = pm.Space()
	fps = pyglet.clock.ClockDisplay()