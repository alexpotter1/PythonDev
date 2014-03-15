# pygame

try:
    import pygame, sys
    pass
except ImportError:
    print("Please install Pygame! ('sudo apt-get install python-pygame')")

pygame.init()
size = width, height = 640,480
black = 0,0,0
white = 255,255,255
red = 255,0,0

gravity = 1.5
momentum = 0.8


screen = pygame.display.set_mode(size)
ball = pygame.Surface((50,50)) # creates new ball surface
ballrectangle = ball.get_rect(center=(50,100)) # attaches collision box to ball
#ball.fill(white)
speed = [2,2] # speed that the ball will move (x,y)
pygame.display.set_caption("Alex's Game")

cross_surface = pygame.image.load('cross.png').convert()


# x,y,radius
pygame.draw.circle(ball,red,[25,25], 25)

# init new clock
clock = pygame.time.Clock()


def clip(value, minval, maxval):
	return min(max(value,minval), maxval)



MouseLeftButton = 0

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
			sys.exit() # allows program to exit and clears memory
        if(event.type == pygame.MOUSEMOTION):
            if event.buttons[MouseLeftButton]: # left button clicked and moving
                relative = event.rel
                speed[0] += float((relative[0]/10))
                speed[1] += float((relative[1]/10))

    speed[1] += gravity

    clock.tick(61)
    fps = int(clock.get_fps())
    myfont = pygame.font.SysFont("arial", 20)
    fpsCounter = myfont.render(("FPS: %i" % fps), 1, white)
    screen.blit(fpsCounter, (0,0))
    pygame.display.flip()


			
    ballrectangle = ballrectangle.move(speed)
    if (ballrectangle.left < 0 or ballrectangle.right > width):
        speed[0] *= momentum # reduces ball energy when colliding with edge of window
        speed[0] = -speed[0]
    if (ballrectangle.top < 0 or ballrectangle.bottom > height):
        speed[1] *= momentum
        speed[1] = -speed[1]



    ballrectangle.left = clip(ballrectangle.left, 0, width)
    ballrectangle.right = clip(ballrectangle.right, 0, width)
    ballrectangle.top = clip(ballrectangle.top, 0, height)
    ballrectangle.bottom = clip(ballrectangle.bottom, 0, height)
			
    screen.fill(black)
    screen.blit(ball,ballrectangle) # moves ball onto screen
    pygame.display.flip() # double buffering, waits until frame is fully drawn
		

