import pygame
import os
from enemies import Enemy

image = pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies", "Mosquito_enemy.png")), (40, 40))


class Mosquito(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Mosquito"
        self.money = 1
        self.max_health = 1
        self.health = self.max_health
        self.imgs = image
