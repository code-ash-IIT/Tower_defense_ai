import pygame
import os
from enemies import Enemy

image = pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies", "Flying_Ghost_enemy.png")), (40, 40))


class Ghost(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Ghost"
        self.money = 1
        self.max_health = 1
        self.health = self.max_health
        self.imgs = image
