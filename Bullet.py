import math,sys,pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("Recources/Projectiles/Bullet.png")
        self.rect = self.image.get_rect()
        self.living = True
        self.speedx = 1
        self.speedy = 1
        self.didBounceX = False
        self.didBounceY = False
        self.maxSpeed = 10
        if direction == "up":
            self.speed = [0, -self.maxSpeed] 
       
        
    def move(self):
        self.rect = self.rect.move(10, 10)
        
    def place(self, pt):
        self.rect.center = pt
     
    def collideBall(self, other):
        if self != other:
            if (self.rect and other.rect) > self.distance(other.rect.center):
                if not self.didBounceX:
                    self.speedx = -self.speedx
                    self.didBouncex = True
                if not self.didBounceY:
                    self.speedy = -self.speedy
                    self.didBounceY = True
        
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
