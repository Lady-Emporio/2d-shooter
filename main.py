import pygame
import pyganim
from game_map import Platform,Camera,camera_configure
from unit import Hero,Hero_body
WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"
pygame.init()
screen = pygame.display.set_mode(DISPLAY)
bg = pygame.Surface((WIN_WIDTH,WIN_HEIGHT))

allForDraw=pygame.sprite.Group()
platforms=pygame.sprite.Group()
hero=Hero(30,30,100,300)
hero_body=Hero_body(30,30,100,300)
allForDraw.add(hero)
allForDraw.add(hero_body)
entities = pygame.sprite.Group() # Все объекты
entities.add(hero)
entities.add(hero_body)


level=open("./Python_copy_paste.txt","r").read().split('\n')

PLATFORM_WIDTH=32
PLATFORM_HEIGHT=32
x=y=0 # координаты
for row in level: # вся строка
	for col in row: # каждый символ
		if col != " ":
			pf = Platform(x,y)
			print(x,y)
			entities.add(pf)
			#platforms.append(pf)
			platforms.add(pf)
		x += PLATFORM_HEIGHT #блоки платформы ставятся на ширине блоков
	y += PLATFORM_HEIGHT    #то же самое и с высотой
	x = 0
total_level_width  = len(level[0])*PLATFORM_WIDTH # Высчитываем фактическую ширину уровня
total_level_height = len(level)*PLATFORM_HEIGHT   # высоту
camera = Camera(camera_configure, total_level_width, total_level_height) 

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
	camera.update(hero)
	#platforms.draw(screen)

	#allForDraw.draw(screen)
	for e in entities:
			screen.blit(e.image, camera.apply(e))
	
	pygame.display.update()
