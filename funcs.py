import pygame,math,sys,os,logging
from pygame.locals import *
import game

p = 180/(math.pi)
def torad(d):
	return d/p
	
def poltorect(angle,speed,r=1):
	if r: angle = angle/p
	(dx,dy) = (speed*math.cos(angle),speed*math.sin(angle))
	return (dx,dy)
	
def recttopol(x,y):
	return math.hypot(x, y), math.atan2(y, x)
def direction_towards((x,y),(dx,dy)):
	nx = dx - x
	ny = dy - y
	angle = math.atan2(ny,nx)
	return angle
	
def distance_to((x1,y1),(x2,y2)):
	return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
	

def addvectors((ad,av),(bd,bv)):
	ax,ay = poltorect(ad,av,0)
	bx,by = poltorect(bd,bv,0)
	cx,cy = ax+bx,ay+by
	
	cs,cd = recttopol(cx,cy)
	return (cd,cs)

	
pi2 = math.pi*2
def normrad(a):
	while a < 0: a += pi2
	while a > pi2: a -= pi2
	return a
	
	
def coord_to_viewport(rect,gx,gy):
	#the viewport tries to center horizontally on the player
	w = game.config.width / 2
	px = max(game.player.x,w) - w
	rect.centerx = gx - px
	rect.centery = gy