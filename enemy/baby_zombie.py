import pygame
import os
from .enemies import Enemy
imgs=[]
enemySize=(45,45)
for x in range(40):
            imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies/4", "baby_zombie"+str(x)+".png")),enemySize))

class Baby_zombie(Enemy):
        
    def __init__(self):
        super().__init__()
        self.imgs=imgs[:]
        self.speed=1
        self.enemySize=enemySize
