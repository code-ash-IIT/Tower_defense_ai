import pygame
import os
from .enemies import Enemy
class Giant(Enemy):
        
    def __init__(self):
        super().__init__()
        self.imgs=[]
        self.enemySize=(50,50)
        for x in range(0,1):
            self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies/3", "giant"+str(x)+".png")),self.enemySize))
