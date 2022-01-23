import pygame
import os
from enemies.enemies import Enemy

imgs = []
enemySize=(60,60)
for x in range(2):
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/Enemies/1", "Mosquito_enemy"+str(x)+".png")),
        (60, 60)))


class Mosquito(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "mosquito"
        self.money = 10
        self.enemySize=enemySize
        self.speed=3.5
        self.max_health = 2
        self.health = self.max_health
        self.imgs = imgs[:]



