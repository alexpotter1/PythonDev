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
	
	
	
	def __init__(self):
		print('inited')
		
	def setColour(self, (r, g, b)):
		self.colour = (r, g, b)
		
	def getColour(self):
		return self.colour
		
	def createBall(self, sizex, sizey, rad):
		self.sizex = sizex
		self.sizey = sizey
		self.rad = rad
		
		ball = pygame.Surface((self.sizex, self.sizey)) # creates new ball surface
		self.ball = ball
		
		pygame.draw.circle(self.ball,self.getColour(),[25,25], self.rad) # x,y,radius
		ballrectangle = self.ball.get_rect(center=([self.sizex/2, self.sizey/2])) # attaches collision box to ball
		self.ballrectangle = ballrectangle	
		
	def Physics(self):
		self.ballrectangle = self.ballrectangle.move(self.speed)
		
		if (self.ballrectangle.left < 0 or self.ballrectangle.right > self.width):
			#speed[0] *= momentum # reduces ball energy when colliding with edge of window
			self.speed[0] = -self.speed[0]
		if (self.ballrectangle.top < 0 or self.ballrectangle.bottom > self.height):
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
    
    
    
def clip(value, minval, maxval):
	return min(max(value,minval), maxval)

def FPS(targetFPS):
    clock.tick_busy_loop(targetFPS)
    fps = int(clock.get_fps())
    myfont = pygame.font.SysFont("arial", 20)
    FPS.fpsCounter = myfont.render(("FPS: %i" % fps), 1, white)
    FPS.fpsCounterRect = FPS.fpsCounter.get_rect(center=(width - (width -40), height -(height-20)))


def draw():
    FPS(60)
    screen.fill(black)
    screen.blit(b1.ball,b1.ballrectangle) # moves ball onto screen
    screen.blit(b2.ball,b2.ballrectangle)
    screen.blit(FPS.fpsCounter, FPS.fpsCounterRect)
    screen.blit(paddle, paddlerectangle)
    pygame.display.flip() # double buffering, waits until frame is fully drawn



b1 = Ball()
b1.setColour(azure)
b1.createBall(50,50,25)

b2 = Ball()
b2.setColour(red)
b2.createBall(50,50,25)


MouseLeftButton = 0
step = 2
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
    
    if paddlerectangle.colliderect(b1.ballrectangle):
		#speed[1] *= momentum
		b1.speed[1] = -b1.speed[1]

    #speed[1] += gravity


    b1.Physics()
		



    if b1.ballrectangle.bottom > height:
        screen.blit(text, textRect)
        pygame.display.update()
        pygame.time.delay(2000)
        b1.ballrectangle.top = 0


    b1.ballrectangle.left = clip(b1.ballrectangle.left, 0, width)
    b1.ballrectangle.right = clip(b1.ballrectangle.right, 0, width)
    b1.ballrectangle.top = clip(b1.ballrectangle.top, 0, height)
    b1.ballrectangle.bottom = clip(b1.ballrectangle.bottom, 0, height)
    
    paddlerectangle.left = clip(paddlerectangle.left, 0, width)
    paddlerectangle.right = clip(paddlerectangle.right, 0,width)
    paddlerectangle.top = clip(paddlerectangle.top, 0, height)
    paddlerectangle.bottom = clip(paddlerectangle.bottom, 0, height)

    draw()

		

