import pygame, sys, random
from KnifeBaddie import KnifeBaddie
from GunBaddie import GunBaddie
from player1 import LenardLangly
from HUD import Text
from HUD import Score
from Button import Button
from BackGround import BackGround
from Level import Level
from Block import Block
from Bullet import Bullet
pygame.init()

clock = pygame.time.Clock()

width = 900 
height = 600
size = width, height


bgColor = r,g,b = 0, 0, 10

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("Recources/Maps/Screen.png").convert()
bgRect = bgImage.get_rect()

gunBaddies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
knifeBaddies = pygame.sprite.Group()
players = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

GunBaddie.containers = (all, gunBaddies)
Bullet.containers = (all, bullets)
KnifeBaddie.containers = (all, knifeBaddies)
LenardLangly.containers = (all, players)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)
Score.containers = (all, hudItems)

spts = [(100,100),
        (800,500),
        (72,505),
        (725,500)]

run = False

startButton = Button([width/2, height-200], 
                     "Recources/Buttons/Button.png", 
                     "Recources/Buttons/ButtonP2.png")


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
        
    BackGround("Recources/Maps/Background V2.png")
    

    player = LenardLangly([width/2, height/2])
<<<<<<< HEAD
=======

    player2 = LenardLangly([width/2, height/2])

>>>>>>> origin/master
    
    
    level = Level(size, 50)
    level.loadLevel("1")

    timer = Score([80, height - 25], "Time: ", 36)
    timerWait = 0
    timerWaitMax = 6



    score = Score([width-80, height-25], "Score: ", 36)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
<<<<<<< HEAD
                if event.key == pygame.K_SPACE:
                    player.attack("Bullet")
=======
                elif event.key == pygame.K_SPACE:
                    projectiles += player.attack("Bullet")
>>>>>>> origin/master
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
        if len(knifeBaddies) < 5:
            if random.randint(0, 1*20) == 0:
                KnifeBaddie("Recources/Enemys/Knife Baddie/paratrooper 1.png",
                          [random.randint(0,3), random.randint(0,3)],
                          spts[random.randint(0,len(spts)-1)])
        if len(gunBaddies) < 5:
            if random.randint(0, 1*20) == 0:
                GunBaddie("Recources/Enemys/Gunman Baddie/Gunman Baddie 1.png",
                          [random.randint(0,3), random.randint(0,3)],
                          spts[random.randint(0,len(spts)-1)])                  
                          
       
        if timerWait < timerWaitMax:
           timerWait += 1
        else:
           timerWait = 0
           timer.increaseScore(.1)
        
        playersHitknifeBaddies = pygame.sprite.groupcollide(players, knifeBaddies, True, False)
        playersHitgunBaddies = pygame.sprite.groupcollide(players, gunBaddies, False, True)
        knifeBaddiesHitknifeBaddies = pygame.sprite.groupcollide(knifeBaddies, knifeBaddies, False, False)
        gunBaddiesHitgunBaddies = pygame.sprite.groupcollide(gunBaddies, gunBaddies, False, False)
        knifeBaddiesHitblocks = pygame.sprite.groupcollide(knifeBaddies, blocks, False, False)
        gunBaddiesHitblocks = pygame.sprite.groupcollide(gunBaddies, blocks, False, False)
        playersHitblocks = pygame.sprite.groupcollide(players, blocks, False, False)
        bulletsHitknifeBaddies = pygame.sprite.groupcollide(bullets, knifeBaddies, True, True)
        bulletsHitgunBaddies = pygame.sprite.groupcollide(bullets, gunBaddies, True, False)
       
        for player in playersHitknifeBaddies:
            for knifeBaddie in playersHitknifeBaddies[player]:
                score.increaseScore(1)
        
        for player in playersHitgunBaddies:
            for gunBaddie in playersHitgunBaddies[player]:
                score.increaseScore(1)
                
        for bully in knifeBaddiesHitknifeBaddies:
            for victem in knifeBaddiesHitknifeBaddies[bully]:
                bully.collideBall(victem)
        
        for bully in gunBaddiesHitgunBaddies:
            for victem in gunBaddiesHitgunBaddies[bully]:
                bully.collideBall(victem) 
                
        for bully in knifeBaddiesHitblocks:
            for victem in knifeBaddiesHitblocks[bully]:
                bully.collideBlock(victem)
        
        for bully in gunBaddiesHitblocks:
            for victem in gunBaddiesHitblocks[bully]:
                bully.collideBlock(victem)
                
        for bully in playersHitblocks:
            for victem in playersHitblocks[bully]:
                bully.collideBlock(victem)
                
        for bully in bulletsHitknifeBaddies:
            for victem in bulletsHitknifeBaddies[bully]:
                bully.collideBall(victem)
                
        for bully in bulletsHitgunBaddies:
            for victem in bulletsHitgunBaddies[bully]:
                bully.collideBall(victem)
        for projectile in projectiles:
            screen.blit(projectile.image, projectile.rect)
        
            
        
        all.update(width, height)
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
