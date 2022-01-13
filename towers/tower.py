import pygame


class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.menu = None
        self.damage = 1
        self.tower_imgs = []

    def draw(self, win):
        img = self.tower_imgs[self.level - 1]
        win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

    def click(self, X, Y):
        if self.x + self.width >= X >= self.x:
            if self.y + self.height >= Y >= self.y:
                return True
        return False

    def sell(self):
        """
        return sell price
        """
        return self.sell_price[self.level - 1]

    def upgrade(self):
        """
        upgrade the tower for given cost
        """
        self.level += 1
        self.damage += 1

    def get_upgrade_cost(self):
        # returns the upgrade cost, if 0 then can't upgrade anymore
        return self.price[self.level - 1]

    def move(self, x, y):
        self.x = x
        self.y = y
