import pygame, math



class KnifeBaddie():
    def __init__(self, image, speed = [0,0], pos = [0,0]):
        self.upImages = [pygame.image.load("Resources/Enemys/Phase/Phase ghostUp1.png"),
                         pygame.image.load("Resources/Objects/Ghosts/Phase/Phase ghostUp2.png"),]
        self.downImages = [pygame.image.load("Resources/Objects/Ghosts/Phase/Phase ghostDN1.png"),
                           pygame.image.load("Resources/Objects/Ghosts/Phase/Phase ghostDN2.png"),]
        self.leftImages = [pygame.image.load("Resources/Objects/Ghosts/Phase/Phase ghostLFT1.png"),
                           pygame.image.load("Resources/Objects/Ghosts/Phase/Phase ghostLFT2.png"),]
        self.rightImages = [pygame.image.load("Resources/Objects/Ghosts/Phase/Phase ghostRGT1.png"),
                            pygame.image.load("Resources/Objects/Ghosts/Phase/Phase ghostRGT2.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 2
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.place(pos)
        self.didBounceX = False
        self.didBounceY = False
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.living = True
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self, width, height):
        self.changed = True
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.animate()
        self.collideEdge(width, height)
        
    def move(self):
        self.rect = self.rect.move(self.speed)
    
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        if self.changed:
            if self.facing == "up":
                self.images = self.upImages
            elif self.facing == "down":
                self.images = self.downImages
            elif self.facing == "right":
                self.images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideEdge(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
                #print "hit xWall"  
    
    def collideGhost(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = True
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = True

    def collidePlayer(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        self.living = False
                        

    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
