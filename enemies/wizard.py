import pygame
import os
from .enemies import Enemy

imgs = []
enemySize=(64,64)
for x in range(3):
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/Enemies/8", "wizard" + str(x) + ".png")),
        (64, 64)))


class Wizard(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "wizard"
        self.money = 3
        self.max_health = 3
        self.speed = 2
        self.enemySize=enemySize
        self.health = self.max_health
        self.imgs = imgs[:]


