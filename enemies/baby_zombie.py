import pygame
import os
from .enemies import Enemy
imgs=[]
enemySize=(45,45)
for x in range(4):
            imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies/4", "baby_zombie"+str(x)+".png")),enemySize))

class Baby_zombie(Enemy):
        
    def __init__(self):
        super().__init__()
        self.name = "baby_zombie"
        self.money = 30
        self.imgs=imgs[:]
        self.speed=0.5
        self.enemySize=enemySize
        self.max_health=4.25
        self.health=self.max_health
