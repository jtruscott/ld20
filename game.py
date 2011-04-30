#i'm going to put all my "static" stuff here like it's global
import pymunk as pm
import world as w
import player as p
import objects as o
import config
import pyglet

title = "Narwhal Jousting!"
objects = []
class ColType:
	player,terrain = range(900,902)
 
def init():
	#Build all the objects we use
	global world,player,space,fps,objects,batch
	batch = pyglet.graphics.Batch()
	world = w.World()
	player = p.Player()
	space = pm.Space()
	pyglet.clock.set_fps_limit(config.fps)
	fps = pyglet.clock.ClockDisplay()
	
	def clock_update(dt):
		for object in objects:
			object.tick()
			
	pyglet.clock.schedule_interval(clock_update,1.0/config.fps)