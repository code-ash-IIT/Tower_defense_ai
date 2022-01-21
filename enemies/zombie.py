import pygame
import os
from .enemies import Enemy

imgs = []
for x in range(2):
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/Enemies/6", "flying_zombie" + str(x) + ".png")),
        (100, 100)))


class Zombie(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "zombie"
        self.money = 200
        self.imgs = imgs[:]
        self.max_health = 100
        self.health = self.max_health




