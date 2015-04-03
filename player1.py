import pygame
from KnifeBaddie import KnifeBaddie

class LenardLangly(KnifeBaddie):
    def __init__(self, pos):
        KnifeBaddie.__init__(self, "Resources/Player/Pax/Normal Pax/Playupr.png", [0,0], pos)
        self.upImages = [pygame.image.load("Resources/Player/Pax/Normal Pax/Playupr.png"),
                         pygame.image.load("Resources/Player/Pax/Normal Pax/Playupl.png"),]
        self.downImages = [pygame.image.load("Resources/Player/Pax/Normal Pax/Playdnl.png"),
                           pygame.image.load("Resources/Player/Pax/Normal Pax/Playdnr.png"),]
        self.leftImages = [pygame.image.load("Resources/Player/Pax/Normal Pax/Playltl.png"),
                           pygame.image.load("Resources/Player/Pax/Normal Pax/Playltr.png"),]
        self.rightImages = [pygame.image.load("Resources/Player/Pax/Normal Pax/Playrtr.png"),
                            pygame.image.load("Resources/Player/Pax/Normal Pax/Playrtl.png")]
        
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = 3
        self.living = True
                
    def update(self, width, height):
        PhaseGhost.update(self, width, height)
        self.animate()
        self.changed = False
        
    
    def collideEdge(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx *= -3
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy *= -3
                self.didBounceY = True
                #print "hit xWall"
    
    def collideSpeed(self, wall):
        if self.rect.right > wall.rect.left and self.rect.left < wall.rect.right:
            if self.rect.bottom > wall.rect.top and self.rect.top < wall.rect.bottom:
                if not self.didBounceX and self.speedx != 0:
                    self.speedx = -self.speedx*1.01
                    self.move()
                    self.speedx *= -1.1
                    print "x"
                    self.didBouncex = True
                if not self.didBounceY and self.speedy != 0:
                    self.speedy = -self.speedy*1.01
                    self.move()
                    self.speedy *= -1.1
                    print "y"
                    self.didBounceY = True
                    print "hit Ball"
    
    def collideWall(self, wall):
        if self.rect.right > wall.rect.left and self.rect.left < wall.rect.right:
            if self.rect.bottom > wall.rect.top and self.rect.top < wall.rect.bottom:
                if not self.didBounceX and self.speedx != 0:
                    self.speedx = -self.speedx*-1.01
                    self.move()
                    self.speedx *= -1
                    print "x"
                    self.didBouncex = True
                if not self.didBounceY and self.speedy != 0:
                    self.speedy = -self.speedy*-1.01
                    self.move()
                    self.speedy *= -1
                    print "y"
                    self.didBounceY = True
                    print "hit Ball"
    
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
                        self.living = False
    
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += .45
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
            
    
    
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0
