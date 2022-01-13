import pygame
import os
from .enemies import Enemy
class Rick(Enemy):
        
    def __init__(self):
        super().__init__()
        self.imgs=[]
        self.speed=1.5
        self.enemySize=(55,55)
        for x in range(20):
            self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies/2", "rick"+str(x)+".png")),self.enemySize))
