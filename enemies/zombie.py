import pygame
import os
from .enemies import Enemy

imgs = []
enemySize=(64,64)
for x in range(2):
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/Enemies/6", "flying_zombie" + str(x) + ".png")),
        enemySize))


class Zombie(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "zombie"
        self.money = 50
        self.speed=3
        self.enemySize=enemySize
        self.imgs = imgs[:]
        self.max_health = 100
        self.health = self.max_health




