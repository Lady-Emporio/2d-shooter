import pygame
import pyganim
DISPLAY=(600,600)
pygame.init()
screen = pygame.display.set_mode(DISPLAY)
bg = pygame.Surface(DISPLAY)
bg.fill(pygame.Color(123,123,123))
timer = pygame.time.Clock()
end_game=False
entities = pygame.sprite.Group()
class Base(pygame.sprite.Sprite):
	def __init__(self,pos_x,pos_y):
		self.pos_x=pos_x;
		self.pos_y=pos_y
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("./Nora.png"),(20,20))
		self.rect = pygame.Rect(self.pos_x, self.pos_y, 20, 20)
		self.value=0
while not end_game:
	timer.tick(60)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			end_game=True
		if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
			left = True
		if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
		   right = True
		if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
		   right = False
		if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
			left = False  
		if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
			top = True
		if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
		   bottom = True
		if e.type == pygame.KEYUP and e.key == pygame.K_UP:
		   top = False
		if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
			bottom = False 
		if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
			x,y=pygame.mouse.get_pos()
			b=Base(x-20,y-20)
			entities.add(b)


	screen.blit(bg, (0,0))
	entities.draw(screen)
	for i in entities:
		if i.value<=120:
			i.value+=1
			i.image=pygame.transform.scale(pygame.image.load("./Nora.png"),(i.value,i.value))
		else:
			entities.remove(i)
			print(i.alive())








	pygame.display.update()