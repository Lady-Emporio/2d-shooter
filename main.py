import pygame
import pyganim
from map import ground_block
WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"


# animObj = pyganim.PygAnimation([('./map/lava.jpg', 200), ('./map/tex_grass.jpg', 200), ('./map/wall.jpg', 600)])
# animObj.play()

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
bg = pygame.Surface((WIN_WIDTH,WIN_HEIGHT))
timer = pygame.time.Clock()
# images=pygame.image.load("./map/lava.jpg")
# img_to_blit = images.convert()
# bg.blit(img_to_blit, (0,0), None,)
block=ground_block(100,100,"lava")

end_game=False
while not end_game:
	timer.tick(60)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			end_game=True
	

	screen.blit(bg, (0,0))
	block.draw(screen)
	block.update(100,100)
	# animObj.blit(bg, (1, 1))
	pygame.display.update()
