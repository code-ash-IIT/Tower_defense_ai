import pygame
import os
from .enemies import Enemy
class Mosquito(Enemy):
    
    def __init__(self):
        super().__init__()
        self.imgs=[]
        self.enemySize=(50,50)
        for x in range(2):
            self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies/1", "Mosquito_enemy"+str(x)+".png")),self.enemySize))
