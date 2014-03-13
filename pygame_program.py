# pygame

import pygame, sys

pygame.init()

size = width, height = 512,512
black = 0,0,0
white = 255,255,255
red = 255,0,0

gravity = 0.9
momentum = 0.9



screen = pygame.display.set_mode(size)
ball = pygame.Surface((50,50)) # creates new ball surface
ballrectangle = ball.get_rect(center=(50,100)) # attaches collision box to ball
#ball.fill(white)
speed = [2,2] # speed that the ball will move (x,y)

pygame.draw.circle(ball,red,[25,25], 25) # x,y,radius


def clip(val, minval, maxval):
	return min(max(val,minval), maxval)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit() # allows program to exit and clears memory
			
	ballrectangle = ballrectangle.move(speed)
	if ballrectangle.left < 0 or ballrectangle.right > 512:
		speed[0] = -speed[0]
	if ballrectangle.top < 0 or ballrectangle.bottom > 512:
		speed[1] = -speed[1]
		
	
			
	speed[1] += gravity
	
	ballrectangle.left = clip(ballrectangle.left, 0, width)
	ballrectangle.right = clip(ballrectangle.right, 0, width)
	ballrectangle.top = clip(ballrectangle.top, 0, height)
	ballrectangle.bottom = clip(ballrectangle.bottom, 0, height)
			
	screen.fill(black)
	screen.blit(ball,ballrectangle) # moves ball onto screen
	pygame.display.flip() # double buffering, waits until frame is fully drawn
		

