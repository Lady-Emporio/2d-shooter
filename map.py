import pygame
import os

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
class ground_block(pygame.sprite.Sprite):
	def __init__(self, x, y,type_ground):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./textures/fx/lava.jpg")
		# self.image = pygame.Surface((100,100))
		# self.image.fill(pygame.Color(255,122,122))
		self.rect = pygame.Rect(x, y, 100, 200)
	def update(self,x,y):
		self.rect.x =y 
		self.rect.y =x
	def draw(self, screen): # Выводим себя на экран
		screen.blit(self.image, (self.rect.x,self.rect.y))
