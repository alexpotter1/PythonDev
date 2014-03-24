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

pygame.display.set_caption("Alex's Game")
screen = pygame.display.set_mode(size)


#paddle = pygame.Surface((60,10))
#paddle.fill(white)
#paddlerectangle = paddle.get_rect(center=((size[0]/2,size[1]-50)))# places paddle rectangle to half of the screen width
#paddlespeed = [2,2]


ball = pygame.Surface((50,50)) # creates new ball surface
ballrectangle = ball.get_rect(center=(50,100)) # attaches collision box to ball
speed = [2,2] # speed that the ball will move (x,y)
pygame.draw.circle(ball,red,[25,25], 25) # x,y,radius

# init new clock
clock = pygame.time.Clock()


#font = pygame.font.SysFont("arial", 40)
#text = font.render("Game Over!", 1, white)
#textRect = text.get_rect(center=((width/2,height/2)))
    
    
    
def clip(value, minval, maxval):
	return min(max(value,minval), maxval)

def FPS(targetFPS):
    clock.tick_busy_loop(targetFPS)
    fps = int(clock.get_fps())
    myfont = pygame.font.SysFont("arial", 20)
    FPS.fpsCounter = myfont.render(("FPS: %i" % fps), 1, white)
    FPS.fpsCounterRect = FPS.fpsCounter.get_rect(center=(width - (width -40), height -(height-20)))


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

    FPS(60)

			
    ballrectangle = ballrectangle.move(speed)
    if (ballrectangle.left < 0 or ballrectangle.right > width):
        speed[0] *= momentum # reduces ball energy when colliding with edge of window
        speed[0] = -speed[0]
    if (ballrectangle.top < 0 or ballrectangle.bottom > height):
        speed[1] *= momentum
        speed[1] = -speed[1]

	#paddlerectangle=paddlerectangle.move(paddlespeed)
	
	#if ballrectangle.colliderect(paddlerectangle):
		#speed[1] *= momentum
		#speed[1] = -speed[1]

    ballrectangle.left = clip(ballrectangle.left, 0, width)
    ballrectangle.right = clip(ballrectangle.right, 0, width)
    ballrectangle.top = clip(ballrectangle.top, 0, height)
    ballrectangle.bottom = clip(ballrectangle.bottom, 0, height)
    
    #paddlerectangle.left = clip(paddlerectangle.left, 0, width)
    #paddlerectangle.right = clip(paddlerectangle.right, 0,width)
    #paddlerectangle.top = clip(paddlerectangle.top, 0, height)
    #paddlerectangle.bottom = clip(paddlerectangle.bottom, 0, height)
			
    screen.fill(black)
    screen.blit(ball,ballrectangle) # moves ball onto screen
    #screen.blit(paddle,paddlerectangle)
    screen.blit(FPS.fpsCounter, FPS.fpsCounterRect)
    #screen.blit(text, textRect)
    pygame.display.flip() # double buffering, waits until frame is fully drawn
		

