import pygame
import pyganim
import math
from game_map import Platform,Camera,camera_configure
from unit import Hero,Hero_body,Shoot_in_mouse,Weapons,Bullet
from const import *


pygame.init()
screen = pygame.display.set_mode(DISPLAY)
bg = pygame.Surface((WIN_WIDTH,WIN_HEIGHT))
allForDraw=pygame.sprite.Group()
platforms=pygame.sprite.Group()
weapons=Weapons(30,30,110,270)
hero=Hero(30,30,100,300)
hero_body=Hero_body(30,30,100,300)
allForDraw.add(hero)
allForDraw.add(hero_body)
entities = pygame.sprite.Group() # Все объекты
entities.add(hero)
entities.add(hero_body)
entities.add(weapons)
Bullet_list = pygame.sprite.Group()
cursor=Shoot_in_mouse()
entities.add(cursor)

level=open("./Python_copy_paste1.txt","r").read().split('\n')
x=y=0 # координаты
for row in level: # вся строка
	for col in row: # каждый символ
		if col != " ":
			pf = Platform(x,y)
			entities.add(pf)
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
		if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
			bullet=Bullet(0,0,weapons.rect.x,weapons.rect.y,cursor=cursor)
			entities.add(bullet)
			Bullet_list.add(bullet)
			
	
	hero.update(left, right,top=top,bottom=bottom)
	hero_body.update(left, right,top=top,bottom=bottom)
	weapons.update(left, right,top=top,bottom=bottom)
	for bullet in Bullet_list:
		bullet.update()
		


	angleA_X, angleA_Y = (hero_body.rect.x+(hero_body.image.get_width()/2), hero_body.rect.y+(hero_body.image.get_height()/2))
	angleB_X, angleB_Y = (cursor.rect.x, cursor.rect.y)
	a = pygame.math.Vector2(angleA_X, angleA_Y)
	b = pygame.math.Vector2(angleB_X, angleB_Y)
	zero = pygame.math.Vector2()
	hero_body.image=pygame.transform.rotate(pygame.image.load("./textures/skins/blue_man/body.png"),90-zero.angle_to(a-b))
	weapons.image=pygame.transform.rotate(pygame.image.load("./textures/weapons/pistol/gun.png"),90-zero.angle_to(a-b))
	
	screen.blit(bg, (0,0))
	w=camera.update(hero_body)
	cursor.update(pygame.mouse.get_pos(),w)




	for e in entities:
			screen.blit(e.image, camera.apply(e))
			#screen.blit(e.image, e.rect.move(-100,-200))
	pygame.display.update()