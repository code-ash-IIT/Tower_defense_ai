import pygame
import os
from .enemies import Enemy
class Mosquito(Enemy):
    imgs=[]
    enemySize=(50,50)
    for x in range(2):
        
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies/1", "Mosquito_enemy"+str(x)+".png")),enemySize))
        
    def __init__(self):
        super().__init__()
