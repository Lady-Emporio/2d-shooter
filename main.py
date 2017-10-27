import pygame
import pyganim
from map import ground_block
from unit import Hero,Hero_body
WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"
pygame.init()
screen = pygame.display.set_mode(DISPLAY)
bg = pygame.Surface((WIN_WIDTH,WIN_HEIGHT))

allForDraw=pygame.sprite.Group()

hero=Hero(30,30,100,300)
hero_body=Hero_body(30,30,100,300)
allForDraw.add(hero)
allForDraw.add(hero_body)






left=right=top=bottom=False
timer = pygame.time.Clock()
end_game=False
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
	

	hero.update(left, right,top=top,bottom=bottom)
	hero_body.update(left, right,top=top,bottom=bottom)
	

	screen.blit(bg, (0,0))
	allForDraw.draw(screen)
	pygame.display.update()
