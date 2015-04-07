import pygame, sys, random
from KnifeBaddie import KnifeBaddie
from player1 import LenardLangly
#from HUD import Text
#from HUD import Score
from Button import Button
from BackGround import BackGround
from Level import Level
from Block import Block

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height


bgColor = r,g,b = 0, 0, 10

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("Recources/Maps/Screen.png").convert()
bgRect = bgImage.get_rect()

knifeBaddies = pygame.sprite.Group()
players = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

KnifeBaddie.containers = (all, knifeBaddies)
LenardLangly.containers = (all, players)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)
#Score.containers = (all, hudItems)



run = False

startButton = Button([width/2, height-200], 
				     "Recources/Buttons/Button.png", 
				     "Recources/Buttons/ButtonP.png")

while True:
	while not run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					run = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				startButton.click(event.pos)
			if event.type == pygame.MOUSEBUTTONUP:
				if startButton.release(event.pos):
					run = True
					
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		screen.blit(startButton.image, startButton.rect)
		pygame.display.flip()
		clock.tick(60)
		
	BackGround("Recources/Maps/Background.png")
	
	player = LenardLangly([width/2, height/2])
	
	
	level = Level(size, 50)
	level.loadLevel("1")

	#timer = Score([80, height - 25], "Time: ", 36)
	#timerWait = 0
	#timerWaitMax = 6

	#score = Score([width-80, height-25], "Score: ", 36)
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("left")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("stop up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("stop right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("stop down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("stop left")
			
		if len(KnifeBaddie) < 10:
			if random.randint(0, 1*60) == 0:
				KnifeBaddie("Recources/Enemys/Knife Baddie/paratrooper 1.png",
						  [random.randint(0,10), random.randint(0,10)],
						  [random.randint(100, width-100), random.randint(100, height-100)])
						  
						  
		#if timerWait < timerWaitMax:
		#	timerWait += 1
		#else:
		#	timerWait = 0
		#	timer.increaseScore(.1)
		
		playersHitknifeBaddies = pygame.sprite.groupcollide(players, knifeBaddies, False, True)
		knifeBaddiesHitknifeBaddies = pygame.sprite.groupcollide(knifeBaddies, knifeBaddies, False, False)
		
		for player in playersHitknifeBaddies:
			for knifeBaddie in playersHitknifeBaddiess[player]:
				score.increaseScore(1)
				
		for bully in knifeBaddiesHitknifeBaddies:
			for victem in knifeBaddiesHitknifeBaddies[bully]:
				bully.collideBall(victem)
		
		all.update(width, height)
		
		dirty = all.draw(screen)
		pygame.display.update(dirty)
		pygame.display.flip()
		clock.tick(60)

