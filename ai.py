import pygame
import os
from enum import Enum

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




class MODE(Enum):
    manual           = 0,
    geneticAlgorithm = 1


GAME_MODE = MODE.manual  # Select which mode to run the game in
PARALLEL_MODE  = False          # Run a game on each processor core (only when visual_mode is off)
COLLECT_WHOLE_GAME_DATA = False  # Game data collection for the GA
COLLECT_INNER_GAME_DATA = False  # "     "
# Q_TRAINING_MODE = True         # Update Q table after every game
VISUAL_MODE    = True          # Display Graphics
READ_FILE      = False          # Read model from file and continue training from it
SAVE_TO_DISK   = False          # Collect and store data
PRINT_GRAPHS   = False          # Prints graphs of score averages

# the game may finally expect the following signature:
#      Game(visualMode, towers, gameRecord, collectInnerGameData, deepQagent)                                                                    




class AIplay:
    def __init__(self, win):
        self.win = win
        game = Game(self.win)
        # pt  = self.place_tower()
        # if(game.run()):
        #     self.place_tower()    #--------- START HERE, NEXT --------
        game.run()
        

    # def place_tower(self):
    #     x,y = points[0]
    #     # ArcherTower(x,y)
    #     Game.moving_object = ArcherTower(x,y)
    #     ArcherTower(x,y).moving = True