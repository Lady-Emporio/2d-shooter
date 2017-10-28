import pygame
import random
import pyganim
from const import *
class PygAni(pyganim.PygAnimation):
	def __init__(self,*arg):
		pyganim.PygAnimation.__init__(self,*arg)
		#self._rate = 1.0 # 2.0 means play the animation twice as fast, 0.5 means twice as slow
		#self._visibility = True # If False, then nothing is drawn when the blit() methods are called



class Base(pygame.sprite.Sprite):
	def __init__(self,width,height,pos_x,pos_y):
		self.width=width;self.height=height;self.pos_x=pos_x;self.pos_y=pos_y
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((self.width,self.height))
		self.image.fill(pygame.Color(100,50,255))
		self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
		self.colorList=[]
		self.move=4

	def update(self):
		pass
	def draw(self, screen,value=0): # Выводим себя на экран
		screen.blit(self.image, (self.rect.x,self.pos_y))


class Hero(Base):
	def __init__ (self,*arg):
		Base.__init__(self,*arg)
		#self.image_real=pygame.image.load("./textures/skins/blue_man/body.png")

		self.image=pygame.image.load("./textures/skins/blue_man/body.png")
		self.image.fill((123,123,123,0))
		self.leg="./textures/skins/blue_man/leg.png"
		self.legback="./textures/skins/blue_man/legback.png"
		self.list_leg_left=((self.leg,300),(self.legback,300))
		self.list_leg_right=((self.legback,300),(self.leg,300))
		self.LegAnimLeft = PygAni(self.list_leg_left)
		self.LegAnimLeft.play()
		#self.LegAnimRight = pyganim.PygAnimation(self.list_leg_right)
		self.LegAnimRight = PygAni(self.list_leg_right)
		self.LegAnimRight.play()
	def update(self,  left, right,top,bottom):
		if top:
			pos_y=-self.move
			self.LegAnimLeft.blit(self.image, (10, 0))
			self.LegAnimRight.blit(self.image, (-10, 0))
		if  bottom:
			pos_y=self.move
			self.LegAnimLeft.blit(self.image, (10, 0))
			self.LegAnimRight.blit(self.image, (-10, 0))
		if left:
			pos_x = -self.move # Лево = x- n
			self.LegAnimLeft.blit(self.image, (10, 0))
			self.LegAnimRight.blit(self.image, (-10, 0))
		if right:
			pos_x = self.move # Право = x + n
			self.LegAnimLeft.blit(self.image, (10, 0))
			self.LegAnimRight.blit(self.image, (-10, 0))
		if not(left or right): # стоим, когда нет указаний идти
			pos_x = 0
		if not (top or bottom):
			pos_y=0
		self.rect.y += pos_y
		self.rect.x += pos_x
	

class Hero_body(Base):
	def __init__ (self,*arg):
		Base.__init__(self,*arg)
		self.image=pygame.image.load("./textures/skins/blue_man/body.png")
		#print(dir(self.image))
		# print(self.image.get_width())
		# print(self.image.get_height())

		#['__class__', '__copy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_pixels_address', 'blit', 'convert', 'convert_alpha', 'copy', 'fill', 'get_abs_offset', 'get_abs_parent', 'get_alpha', 'get_at', 'get_at_mapped', 'get_bitsize', 'get_bounding_rect', 'get_buffer', 'get_bytesize', 'get_clip', 'get_colorkey', 'get_flags', 'get_height', 'get_locked', 'get_locks', 'get_losses', 'get_masks', 'get_offset', 'get_palette', 'get_palette_at', 'get_parent', 'get_pitch', 'get_rect', 'get_shifts', 'get_size', 'get_view', 'get_width', 'lock', 'map_rgb', 'mustlock', 'scroll', 'set_alpha', 'set_at', 'set_clip', 'set_colorkey', 'set_masks', 'set_palette', 'set_palette_at', 'set_shifts', 'subsurface', 'unlock', 'unmap_rgb']
		#self.image=pygame.transform.rotate(pygame.image.load("./textures/skins/blue_man/body.png"),90)
	def update(self,  left, right,top,bottom):
		if top:
			pos_y=-self.move
		if  bottom:
			pos_y=self.move
		if left:
			pos_x = -self.move # Лево = x- n
		if right:
			pos_x = self.move # Право = x + n
		if not(left or right): # стоим, когда нет указаний идти
			pos_x = 0
		if not (top or bottom):
			pos_y=0
		self.rect.y += pos_y
		self.rect.x += pos_x

class Shoot_in_mouse(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.segment_width=10
		self.segment_height=10
		self.image = pygame.Surface([self.segment_width, self.segment_height])
		self.image.fill((50,240,113))
		self.rect = pygame.Rect(40, 40, self.segment_width, self.segment_height)
	def draw(self, screen): # Выводим себя на экран
		screen.blit(self.image, (self.rect.x,self.rect.y))
	def update(self,value,w):
		self.rect.x = value[0]-w[0]
		self.rect.y = value[1]-w[1]




class Weapons(Base):
	def __init__ (self,*arg):
		Base.__init__(self,*arg)
		self.image=pygame.image.load("./textures/weapons/pistol/gun.png")
	def update(self,  left, right,top,bottom):
		if top:
			pos_y=-self.move
		if  bottom:
			pos_y=self.move
		if left:
			pos_x = -self.move # Лево = x- n
		if right:
			pos_x = self.move # Право = x + n
		if not(left or right): # стоим, когда нет указаний идти
			pos_x = 0
		if not (top or bottom):
			pos_y=0
		self.rect.y += pos_y
		self.rect.x += pos_x



class Bullet(Base):
	def __init__ (self,*arg,cursor):
		Base.__init__(self,*arg)
		self.target_x,self.target_y=cursor.rect.x,cursor.rect.y
		self.image=pygame.image.load("./textures/weapons/pistol/bullet.png")
		self.move=1
	def update(self):
		pos_x=0
		pos_y=0
		if self.rect.x<self.target_x:
			pos_x=self.move
		elif self.rect.x>self.target_x:
			pos_x=-self.move

		if self.rect.y<self.target_y:
			pos_y=self.move
		elif self.rect.y>self.target_y:
			pos_y=-self.move
		self.rect.x+=pos_x
		self.rect.y+=pos_y

