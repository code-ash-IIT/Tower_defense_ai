import pygame
import os
from .enemies import Enemy
imgs=[]
enemySize=(75,75)
for x in range(19):
    imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies/3", "giant"+str(x)+".png")),enemySize))
class Giant(Enemy):
        
    def __init__(self):
        super().__init__()
        self.imgs=imgs
        self.speed=1
        self.enemySize=enemySize
