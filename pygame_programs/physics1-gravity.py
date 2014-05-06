# pygame

try:
    import pygame
    pass
except ImportError:
    print("Please install Pygame! ('sudo apt-get install python-pygame')")

class Ball():
	position = [0,0]
	colour = (255,255,255)
	speed = [2,2] # speed that the ball will move (x,y)
	width = 640
	height = 480 # symlink to size in main program 
	
	
	def __init__(self, speed, colour, sizex, sizey, posx, posy, rad):
		self.colour = colour
		self.speed = speed
		
		self.sizex = sizex
		self.sizey = sizey
		self.rad = rad
		self.posx = posx
		self.posy = posy
		
		ball = pygame.Surface((self.sizex, self.sizey)) # creates new ball surface
		self.ball = ball
		
		pygame.draw.circle(self.ball,self.getColour(),[self.sizex/2, self.sizey/2], self.rad) # x,y,radius
		self.ballrectangle = self.ball.get_rect() # attaches collision box to ball
		self.ballrectangle.center = [self.posx,self.posy]
		print("Ball created")
		print('inited')

		
	def getColour(self):
		return self.colour
		
	def clip(self, value, minval, maxval):
		return min(max(value,minval), maxval)
		
	def physics(self):
		self.ballrectangle = self.ballrectangle.move(self.speed)
		
		if (self.ballrectangle.left < 0 or self.ballrectangle.right > self.width):
			#speed[0] *= momentum # reduces ball energy when colliding with edge of window
			self.speed[0] = -self.speed[0]
		if (self.ballrectangle.top < 0 or self.ballrectangle.bottom > self.height):
			#speed[1] *= momentum
			self.speed[1] = -self.speed[1]
			
		if self.ballrectangle.bottom > height:
			screen.blit(text, textRect)
			pygame.display.update()
			pygame.time.delay(2000)
			self.ballrectangle.top = 0
			
		self.ballrectangle.left = self.clip(self.ballrectangle.left, 0, width)
		self.ballrectangle.right = self.clip(self.ballrectangle.right, 0, width)
		self.ballrectangle.top = self.clip(self.ballrectangle.top, 0, height)
		self.ballrectangle.bottom = self.clip(self.ballrectangle.bottom, 0, height)
		
		if paddlerectangle.colliderect(self.ballrectangle):
			#speed[1] *= momentum
			self.speed[1] = -self.speed[1]
			
		
		
	

		

	
		
		
pygame.init()
size = width, height = 640,480

black = 0,0,0
white = 255,255,255
azure = 0,127,255
red = 255,0,0



pygame.display.set_caption("Alex's Game")
screen = pygame.display.set_mode(size)


paddle = pygame.Surface((60,10))
paddle.fill(white)
paddlerectangle = paddle.get_rect(center=((size[0]/2,size[1]-50)))# places paddle rectangle to half of the screen width



# init new clock
clock = pygame.time.Clock()


font = pygame.font.SysFont("arial", 40)
text = font.render("Game Over!", 1, white)
textRect = text.get_rect(center=((width/2,height/2)))
    
collisionsChecked = []  
  
def checkIfCollided(collider):
	notFound = False
	for c in collisionsChecked:
		if c == collider:
			return True
	return False    


def FPS(targetFPS):
    clock.tick_busy_loop(targetFPS)
    fps = int(clock.get_fps())
    myfont = pygame.font.SysFont("arial", 20)
    FPS.fpsCounter = myfont.render(("FPS: %i" % fps), 1, white)
    FPS.fpsCounterRect = FPS.fpsCounter.get_rect(center=(width - (width -40), height -(height-20)))


def draw():
    FPS(60)
    screen.fill(black)
    screen.blit(FPS.fpsCounter, FPS.fpsCounterRect)
    screen.blit(paddle, paddlerectangle)

    
    for ball in balls:
		screen.blit(ball.ball, ball.ballrectangle)
	
    pygame.display.flip()


balls = [Ball([3,3],red,50,50,300,300,25),Ball([2,2],azure,50,50,100,100,25)]








MouseLeftButton = 0
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        #if(event.type == pygame.MOUSEMOTION):
            #if event.buttons[MouseLeftButton]: # left button clicked and moving
                #relative = event.rel
                #speed[0] += float((relative[0]/10))
                #speed[1] += float((relative[1]/10))


	
	position = pygame.mouse.get_pos()
	x = int(position[0])
    paddlerectangle.right = x
    

    #speed[1] += gravity
    collisionsChecked = []

    for ball in balls:
		ball.physics()
		
		for collision in balls:
			if checkIfCollided(collision) == False:
				if collision != ball:
					if ball.ballrectangle.colliderect(collision.ballrectangle):
						collisionsChecked.append(ball)
						collisionsChecked.append(collision)
						ball.speed[1] = -ball.speed[1]
						collision.speed[1] = -collision.speed[1]
						
						ball.speed[0] = -ball.speed[0]
						collision.speed[0] = -collision.speed[0]
				
		
	
		
	
    
    paddlerectangle.left = balls[0].clip(paddlerectangle.left, 0, width)
    paddlerectangle.right = balls[0].clip(paddlerectangle.right, 0,width)
    paddlerectangle.top = balls[0].clip(paddlerectangle.top, 0, height)
    paddlerectangle.bottom = balls[0].clip(paddlerectangle.bottom, 0, height)

    draw()
    
    

		

