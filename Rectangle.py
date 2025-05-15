# Importing pygame module
import pygame
from pygame.locals import *

class Rectangle:
    #class fields
    # size, color,
    def __init__(self,size,color,thickness,window):
        self.size = size
        self.color = color
        self.health=100
        pygame.draw.rect(window,color,size, thickness)
        pygame.display.update()
    