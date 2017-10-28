import pygame
import pyganim
import math
from game_map import Platform,Camera,camera_configure
from unit import Hero,Hero_body,Shoot_in_mouse
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
cursor=Shoot_in_mouse()
entities.add(cursor)

level=open("./Python_copy_paste1.txt","r").read().split('\n')

PLATFORM_WIDTH=32
PLATFORM_HEIGHT=32
x=y=0 # координаты
for row in level: # вся строка
	for col in row: # каждый символ
		if col != " ":
			pf = Platform(x,y)
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




# class Vec2d(pygame.math.Vector2):
# 	def __init__(self, x_or_pair, y = None)
# 	pygame.math.Vector2.__init__(self, x_or_pair, y = None)

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
	



	# m_x,m_y=pygame.mouse.get_pos()
	# # wtf=((hero_body.rect.x,m_x),(hero_body.rect.y,m_y))
	# side_a=m_x-hero_body.rect.x
	# side_b=m_y-hero_body.rect.y
	# # if side_a<0:
	# # 	side_a=0
	# # if side_b<0:
	# # 	side_b=0
	# # hypot_to_herobody_and_mouse=math.hypot(side_a,side_b ) 
	# # c=hypot_to_herobody_and_mouse
	# # try:
	# # 	w=math.acos((side_a ** 2 - side_b ** 2 - c ** 2)/(-2 * side_b * c)) #26
	# # except ZeroDivisionError as h:
	# # 	w=0
	# # hero_body.image=pygame.transform.rotate(pygame.image.load("./textures/skins/blue_man/body.png"),math.degrees(w)-180)
	# angleA_X, angleA_Y = (hero_body.rect.x+(hero_body.image.get_width()/2), hero_body.rect.y+(hero_body.image.get_height()/2))
	# angleB_X, angleB_Y = (m_x, m_y)

	# a = pygame.math.Vector2(angleA_X, angleA_Y)
	# b = pygame.math.Vector2(angleB_X, angleB_Y)

	# zero = pygame.math.Vector2()

	# #print( zero.angle_to(a-b) )

	# hero_body.image=pygame.transform.rotate(pygame.image.load("./textures/skins/blue_man/body.png"),90-zero.angle_to(a-b))




	#cursor.update(pygame.mouse.get_pos())
	screen.blit(bg, (0,0))
	w=camera.update(hero)
	cursor.update(pygame.mouse.get_pos(),w)
	#platforms.draw(screen)

	#allForDraw.draw(screen)
	for e in entities:
			screen.blit(e.image, camera.apply(e))
			#screen.blit(e.image, e.rect.move(-100,-200))
	#print(camera.apply(cursor))
	
	print(cursor.rect.x,cursor.rect.y)
	pygame.display.update()
	#cursor_group.remove(m)
