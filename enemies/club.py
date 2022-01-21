import pygame
import os
from .enemies import Enemy

imgs = []
for x in range(2):
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/Enemies/5", "furious" + str(x) + ".png")),
        (64, 64)))


class Club(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "club"
        self.money = 5
        self.imgs = imgs[:]
        self.max_health = 5
        self.health = self.max_health



