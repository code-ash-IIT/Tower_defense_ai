import pygame
import os
from .enemies import Enemy
class Baby_zombie(Enemy):
        
    def __init__(self):
        super().__init__()
        self.imgs=[]
        self.speed=2.5
        self.enemySize=(45,45)
        for x in range(40):
            self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies/4", "baby_zombie"+str(x)+".png")),self.enemySize))
