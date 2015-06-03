import pygame, sys, random
from KnifeBaddie import KnifeBaddie
from GunBaddie import GunBaddie
from player1 import LenardLangly
from KnifeGOD import KnifeGod
from Player2 import JackSherman
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
knifeGods = pygame.sprite.Group()
players = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
playerzs = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

GunBaddie.containers = (all, gunBaddies)
Bullet.containers = (all, bullets)
KnifeBaddie.containers = (all, knifeBaddies)
KnifeGod.containers = (all, knifeGods)
LenardLangly.containers = (all, players)
JackSherman.containers = (all, playerzs)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)
Score.containers = (all, hudItems)

Knspts = [(100,100),
        (800,500),
        (72,505),
        (725,500)]

Gnspts = [(400,500)]

Kgspts = [(150,150)]

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
        
    BackGround("Recources/Maps/Map Limbo.png")
    
    player = LenardLangly([width/2, height/2])
    
    player2 = JackSherman([width/2, height/2])

    projectiles = []
    
    KnifeGod.health = 20
    
    level = Level(size, 50)
    level.loadLevel("1")

    timer = Score([80, height - 25], "Time: ", 36)
    timerWait = 0
    timerWaitMax = 1



    score = Score([width-80, height-25], "Score: ", 36)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.go("up")
                elif event.key == pygame.K_d:
                    player.go("right")
                elif event.key == pygame.K_s:
                    player.go("down")
                elif event.key == pygame.K_a:
                    player.go("left")
                if event.key == pygame.K_SPACE:
                    player.attack("Bullet")
                elif event.key == pygame.K_UP:
                    player2.go("up")
                elif event.key == pygame.K_RIGHT:
                    player2.go("right")
                elif event.key == pygame.K_DOWN:
                    player2.go("down")
                elif event.key == pygame.K_LEFT:
                    player2.go("left")
                if event.key == pygame.K_KP0:
                    player2.attack("Bullet")
                   

                elif event.key == pygame.K_SPACE:
                    projectiles += player.attack("Bullet")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.go("stop up")
                elif event.key == pygame.K_d:
                    player.go("stop right")
                elif event.key == pygame.K_s:
                    player.go("stop down")
                elif event.key == pygame.K_a:
                    player.go("stop left")   
                elif event.key == pygame.K_UP:
                    player2.go("stop up")
                elif event.key == pygame.K_RIGHT:
                    player2.go("stop right")
                elif event.key == pygame.K_DOWN:
                    player2.go("stop down")
                elif event.key == pygame.K_LEFT:
                    player2.go("stop left")
        
        
        
        
        
        if len(knifeBaddies) < 5:
            if random.randint(0, 1*20) == 0:
                KnifeBaddie("Recources/Enemys/Knife Baddie/paratrooper 1.png",
                          [random.randint(0,3), random.randint(0,3)],
                          Knspts[random.randint(0,len(Knspts)-1)])
        if len(gunBaddies) < 5:
            if random.randint(0, 1*20) == 0:
                GunBaddie("Recources/Enemys/Gunman Baddie/Gunman Baddie 1.png",
                          [random.randint(0,3), random.randint(0,3)], 
                          Gnspts[random.randint(0,len(Gnspts)-1)])                  
        if len(knifeGods) < 1:
            if random.randint(0, 1*20) == 0:
                KnifeGod("Recources/Enemys/Knife God/KnifegodS.png",
                          [random.randint(0,3), random.randint(0,3)],
                          Kgspts[random.randint(0,len(Kgspts)-1)])                  
       
        if timerWait < timerWaitMax:
           timerWait += 1
        else:
           timerWait = 0
           timer.increaseScore(.1)
        
        playersHitknifeBaddies = pygame.sprite.groupcollide(players, knifeBaddies, True, True)
        playerzsHitknifeBaddies = pygame.sprite.groupcollide(playerzs, knifeBaddies, True, True)
        playersHitknifeGods = pygame.sprite.groupcollide(players, knifeGods, True, False)
        playerzsHitknifeGods = pygame.sprite.groupcollide(playerzs, knifeGods, True, False)
        playersHitgunBaddies = pygame.sprite.groupcollide(players, gunBaddies, False, True)
        playerzsHitgunBaddies = pygame.sprite.groupcollide(playerzs, gunBaddies, False, True)
        knifeBaddiesHitknifeBaddies = pygame.sprite.groupcollide(knifeBaddies, knifeBaddies, False, False)
        gunBaddiesHitgunBaddies = pygame.sprite.groupcollide(gunBaddies, gunBaddies, False, False)
        gunBaddiesHitplayers = pygame.sprite.groupcollide(gunBaddies, players, True, False)
        knifeBaddiesHitblocks = pygame.sprite.groupcollide(knifeBaddies, blocks, False, False)
        knifeGodsHitblocks = pygame.sprite.groupcollide(knifeGods, blocks, False, False)
        gunBaddiesHitblocks = pygame.sprite.groupcollide(gunBaddies, blocks, False, False)
        playersHitblocks = pygame.sprite.groupcollide(players, blocks, False, False)
        playerzsHitblocks = pygame.sprite.groupcollide(playerzs, blocks, False, False)
        bulletsHitknifeBaddies = pygame.sprite.groupcollide(bullets, knifeBaddies, True, True)
        bulletsHitknifeGods = pygame.sprite.groupcollide(bullets, knifeGods, True, False)
        bulletsHitgunBaddies = pygame.sprite.groupcollide(bullets, gunBaddies, True, False)
        bulletsHitblocks = pygame.sprite.groupcollide(bullets, blocks, True, False)
        
       
        print players.sprites()
        for player in playersHitknifeBaddies:
            for knifeBaddie in playersHitknifeBaddies[player]:
                player.living = False
                print player
                
        for player in playersHitknifeGods:
            for knifeGod in playersHitknifeGods[player]:
                player.living = False
                print player
        
        for player in playersHitgunBaddies:
            for gunBaddie in playersHitgunBaddies[player]:
                score.increaseScore(1)
                
        for player in playersHitknifeBaddies:
            for knifeBaddie in playersHitknifeBaddies[player]:
                player2.living = False
                
        for player in playersHitknifeGods:
            for knifeGods in playersHitknifeGods[player]:
                player2.living = False
        
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

        for bully in knifeGodsHitblocks:
            for victem in knifeGodsHitblocks[bully]:
                bully.collideBlock(victem)
        
        for bully in gunBaddiesHitblocks:
            for victem in gunBaddiesHitblocks[bully]:
                bully.collideBlock(victem)
                
        for bully in playersHitblocks:
            for victem in playersHitblocks[bully]:
                bully.collideBlock(victem)
                
        for bully in playerzsHitblocks:
            for victem in playerzsHitblocks[bully]:
                bully.collideBlock(victem)
                
        for bully in bulletsHitknifeBaddies:
            for victem in bulletsHitknifeBaddies[bully]:
                bully.collideBall(victem)
                score.increaseScore(1)
                
        for bully in bulletsHitknifeGods:
            for victem in bulletsHitknifeGods[bully]:
                bully.collideBall(victem)
                KnifeGod.health -= 1
                
        for bully in bulletsHitgunBaddies:
            for victem in bulletsHitgunBaddies[bully]:
                bully.collideBall(victem)
        
        for bully in bulletsHitblocks:
            for victem in bulletsHitblocks[bully]:
                bully.collideBlock(victem)
                score.increaseScore(0)


        
        print KnifeGod.health
        all.update(width, height)
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
