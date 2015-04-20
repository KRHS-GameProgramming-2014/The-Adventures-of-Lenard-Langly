import math,sys,pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("Recources/Projectiles/Bullet.png")
        self.rect = self.image.get_rect()
        self.speedx = 1
        self.speedy = 0
        self.living = True
        self.speed = [self.speedx, self.speedy] 
       
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def place(self, pt):
        self.rect.center = pt
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.move()
        
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
