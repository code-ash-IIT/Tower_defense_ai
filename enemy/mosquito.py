import pygame
import os
from .enemies import Enemy
imgs=[]
enemySize=(60,60)
for x in range(2):
    imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies/1", "Mosquito_enemy"+str(x)+".png")),enemySize))
class Mosquito(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs=imgs[:]
        self.enemySize=enemySize
        self.speed=1
