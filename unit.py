import pygame
import random
import pyganim
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
		self.image=pygame.image.load("./textures/skins/blue_man/body.png")
		self.leg="./textures/skins/blue_man/leg.png"
		self.legback="./textures/skins/blue_man/legback.png"
		self.list_leg_left=((self.leg,300),(self.legback,300))
		self.list_leg_right=((self.legback,300),(self.leg,300))
		self.LegAnimLeft = pyganim.PygAnimation(self.list_leg_left)
		self.LegAnimLeft.play()
		self.LegAnimRight = pyganim.PygAnimation(self.list_leg_right)
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
	