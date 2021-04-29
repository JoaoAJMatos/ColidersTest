import pygame, sys
import random

def randInt():
	return random.randint(0, 800)

def bouncing_rect():
	global x_speed, y_speed, second_rect_y_speed

	moving_rect.x += x_speed
	moving_rect.y += y_speed

	#Colision with the screen borders
	if moving_rect.right >= screen_width or moving_rect.left <= 0: #If the rectangle touches the borders:
		x_speed *= -1 #Then the x speed is inverted

	if moving_rect.bottom >= screen_height or moving_rect.top <= 0:
		y_speed *= -1 #The y speed is inverted                           

	
	#Moving the second rectangle
	second_rect.y += second_rect_y_speed
	if second_rect.top <= 0 or second_rect.bottom >= screen_height:
		second_rect_y_speed *= -1


	#Colision with rect
	if moving_rect.colliderect(second_rect):
		if abs(second_rect.top - moving_rect.bottom) < 10 and y_speed > 0: #10 is the colision tolerance, as the pixels move too fast
			y_speed *= -1

		if abs(second_rect.bottom - moving_rect.top) < 10 and y_speed < 0: 
			y_speed *= -1

		if abs(second_rect.right - moving_rect.left) < 10 and x_speed < 0: 
			x_speed *= -1

		if abs(second_rect.left - moving_rect.right) < 10 and x_speed > 0: 
			x_speed *= -1



	pygame.draw.rect(screen, (255,255,255), moving_rect)
	pygame.draw.rect(screen, (255,100,0), second_rect)


pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))

moving_rect = pygame.Rect(randInt(),randInt(),100,100)
x_speed, y_speed = 5, 4

second_rect = pygame.Rect(300,300,200,100)
second_rect_y_speed = 2


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


	screen.fill((30,30,30))
	bouncing_rect()
	pygame.display.flip()
	clock.tick(60)