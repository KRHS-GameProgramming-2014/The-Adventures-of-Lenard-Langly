#Code from Riley Skinner and Brian Calagahan
#https://code.google.com/p/thetempleoflobsterman/
#spooners code
import pygame, math

class Wall():
        def __init__(self, tl, br):
                self.image = pygame.image.load("Recources/Maps/Wall.png")
                width = br[0] - tl[0]
                height = br[1] - tl[1]
                self.image = pygame.transform.scale(self.image, [width, height])        
                self.rect = self.image.get_rect(topleft = tl)
