import math,sys,pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("Recources/Projectiles/Bullet.png")
        self.rect = self.image.get_rect()
        self.living = True
        self.maxSpeed = 10
        if direction == "up":
            self.speed = [0, -self.maxSpeed] 
        elif direction == "down":
            self.speed = [0, self.maxSpeed] 
        elif direction == "right":
            self.speed = [self.maxSpeed, 0] 
        elif direction == "left":
            self.speed = [-self.maxSpeed, 0] 
        self.place(pos)
        
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def place(self, pt):
        self.rect.center = pt
     
    def collideBall(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.rect and other.rect) > self.distance(other.rect.center):
                        self.living = False
                        return True
        
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
