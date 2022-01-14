import os
import pygame
import math
import time
from .tower import Tower

tower_imgs = []
archer_imgs = []
for x in range(1, 4):
    tower_imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/archer_towers/tower/tower_" + str(x) + ".png")), (64, 64)))

for x in range(1, 2):
    archer_imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/archer_towers/tower_top/tower_top_" + str(x) + ".png")),
        (40, 40)))


class ArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs[:]
        self.archer_imgs = archer_imgs[:]
        self.tower_count = 0
        self.range = 100
        self.inRange = False
        self.archer_count = 0
        self.left = True
        self.timer = time.time()
        self.damage=1

    def draw(self, win):
        # draw range circle (drawn first so that it is present below the archer tower)
        surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (0, 150, 230, 70), (self.range, self.range), self.range, 0)
        win.blit(surface, (self.x - self.range, self.y - self.range))

        # draws tower
        super().draw(win)

        if self.archer_count >= len(self.archer_imgs) * 30:
            self.archer_count = 0

        # incase if we had multiple images we the animation(of archer) would only be seen when the enemy was in range
        if self.inRange:
            archer = self.archer_imgs[self.archer_count // 30]
            win.blit(archer, ((self.x + self.width / 2) - 20, (self.y - archer.get_height() - 20)))
            self.archer_count += 1
        else:
            self.archer_count = 0
            archer = self.archer_imgs[self.archer_count // 30]
            win.blit(archer, ((self.x + self.width / 2) - 20, (self.y - archer.get_height() - 20)))

    def change_range(self, r):
        """
        change range of archer tower
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):

        # attacks enemy in the enemy list, modify list
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            dist = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dist < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        # sort the enemies according to distance from the archer tower
        enemy_closest.sort(key=lambda x: x.x)

        # check if any enemy is near the range of tower
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]

            # shoots after every 0.5 seconds
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if first_enemy.hit():
                    enemies.remove(first_enemy)

            # checking if we need to flip the image of the archer
            if first_enemy.x < self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x > self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)


canon_imgs = []
canon_imgs.append(pygame.transform.scale(
    pygame.image.load(os.path.join("assets/archer_towers/canon/canon.png")), (50, 50)))


class Canon(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = canon_imgs[:]
        self.canon_imgs = canon_imgs[:]
        self.tower_count = 0
        self.range = 100
        self.inRange = False
        self.archer_count = 0
        self.left = True
        self.timer = time.time()
        self.damage=1.5

    def draw(self, win):
        # draw range circle (drawn first so that it is present below the archer tower)
        surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (0, 150, 230, 70), (self.range, self.range), self.range, 0)
        win.blit(surface, (self.x - self.range, self.y - self.range))

        super().draw(win)

    def change_range(self, r):
        """
        change range of archer tower
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):
        # attacks enemy in the enemy list, modify list
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            dist = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dist < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        # sort the enemies according to distance from the archer tower
        enemy_closest.sort(key=lambda x: x.x)

        # check if any enemy is near the range of tower
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            # shoots after every 0.5 seconds
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if first_enemy.hit(self.damage):
                    enemies.remove(first_enemy)

            if first_enemy.x < self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.canon_imgs):
                    self.canon_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x > self.x:
                self.left = False
                for x, img in enumerate(self.canon_imgs):
                    self.canon_imgs[x] = pygame.transform.flip(img, True, False)
