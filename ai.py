import pygame
import os
from enemies.mosquito import Mosquito
from enemies.club import Club
from enemies.wizard import Wizard
from enemies.zombie import Zombie
from enemies.rick import Rick
from enemies.giant import Giant
from enemies.baby_zombie import Baby_zombie
from towers.archerTower import ArcherTower, ArcherTowerShort
from towers.supportTower import DamageTower, RangeTower
from menu.menu import VerticalMenu, PlayPauseButton
import time
import random
from Tower_defense import Game

# model building will start here----

points = [(161, 352), (309, 336), (357, 224), (789, 313), (766, 428), (562, 416)] #points where towers will be placed by AI 
                                                                                # according to bg

class AIplay:
    def __init__(self, win):
        self.win = win
        game = Game(self.win)
        # pt  = self.place_tower()
        # if(game.run()):
        #     self.place_tower()    #--------- START HERE, NEXT --------
        game.run()
        

    def place_tower(self):
        x,y = points[0]
        # ArcherTower(x,y)
        Game.moving_object = ArcherTower(x,y)
        ArcherTower(x,y).moving = True