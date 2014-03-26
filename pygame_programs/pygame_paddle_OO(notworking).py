# Filename: pygame_PADDLE.py

try:
	import pygame, sys
	pass
except ImportError:
	print("Please install Pygame")
	
class ProgramInit():
	def __init__(self, screenx, screeny, displayCaption): # 4 passable args
		self.screenx = screenx
		self.screeny = screeny
		self.displayCaption = displayCaption # referencing args so they can be passed on
	
	def pygame_windowInit(self): # self automatically passes args defined in __init__ I think :)
		pygame.init() # inits Pygame
		
		pygame.display.set_caption(str(self.displayCaption)) # sets up caption based on arguments passed to class constructor
		screen = pygame.display.set_mode([self.screenx, self.screeny]) # sets screen size based on arguments passed to class constructor
		self.screen = screen
		
		
		
		clock = pygame.time.Clock() # init a new reference to Pygame's clock for FPS counting
		self.clock = clock
	
class ProgramMain():
	def __init__(self, targetFPS, gravity, momentum):
		self.targetFPS = targetFPS
		self.gravity = gravity
		self.momentum = momentum
		speed = [2,2]
		self.speed = speed
		MouseLeftButton = 0
		self.MouseLeftButton = MouseLeftButton
		
			
	def clip(value, minval, maxval):
		return min(max(value,minval), maxval)
	
	def FPS(self):
		width = ProgramInit.self.screenx
		height = ProgramInit.self.screeny
		
		
		self.clock.tick(self.targetFPS)
		fps = int(self.clock.get_fps())
		
		font = pygame.font.SysFont("helvetica", 20)
		fpscounter = font.render(("FPS: %i" % fps), True, (255,255,255))
		
		self.fpscounter = fpscounter
		fpscounterrect = self.fpscounter.get_rect(center=(width - (width -40), height -(height-20)))
		self.fpscounterrect = fpscounterrect # referencing this to self so HOPEFULLY we are able to access from other places in the class
		
	def pygame_blit(self, Object, ObjectRect):
		self.Object = Object
		self.ObjectRect = ObjectRect
		
		black = (0,0,0)
		ProgramInit.pygame_windowInit.screen.fill(black)
		ProgramInit.pygame_windowInit.screen.blit(Object, ObjectRect)
		
	def Main(self): # this needs to be called last
		ball = pygame.Surface((50,50))
		ballrectangle = ball.get_rect(center=(ProgramInit.screenx - (ProgramInit.screenx - 600), ProgramInit.screeny - (ProgramInit.screeny - 400)))
		pygame.draw.circle(ball,(255,0,0),[25,25],25)
		
		
		while True:
			for event in pygame.event.get():
				if (event.type == pygame.QUIT):
					sys.exit() # allows program to exit and clears memory
				if(event.type == pygame.MOUSEMOTION):
					if event.buttons[self.MouseLeftButton]: # left button clicked and moving
						relative = event.rel
						self.speed[0] += float((relative[0]/10))
						self.speed[1] += float((relative[1]/10))
                        
			self.speed[1] += self.gravity
			FPS(60)
            
			ballrectangle = ballrectangle.move(self.speed)
			pygame_blit(ball,ballrectangle)
			pygame.display.flip()
            
                        
            
		
		
		
		
		
		
		
	
	
	
	
	
p = ProgramInit(640, 480, "Alex's Game")
p.pygame_windowInit()

m = ProgramMain(60,1.5,0.8)
m.Main()




		
		
		

