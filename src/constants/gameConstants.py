from enemies.zombie import Zombie
from enemies.dino import Dino
from enemies.dragon import Dragon
from enemies.robot import Robot
from enemies.wizard import Wizard
from enemies.warrior import Warrior
from enemies.trump import Trump
from enemies.attackingEnemy import AttackingEnemy

from towers.squareTower import SquareTower
from towers.wizardTower import WizardTower
from towers.birdCastle import BirdCastle
from towers.obelisk import Obelisk
from towers.pyramid import Pyramid
from towers.city import City
from towers.igloo import Igloo

FULLSCREEN_MODE = False     #Display in fullscreen (runs better for high res screens)
PLAY_BG_MUSIC = False        #Set false to turn music off

SHOW_CLICKS = False         #If true will display dots where clicked, and print the coordinate in terminal
SHOW_PATH_BOUNDS = True     #If true will display bounds to enemy path

# Locations where towers may be placed
TOWER_GRID = [(30, 491), (29, 585), (23, 686), (103, 540), (104, 626), (109, 707), (194, 553), (285, 541), (376, 502), (406, 400), (196, 659), (197, 766), (277, 652), (293, 761), (360, 611), (376, 715), (456, 754), (446, 623), (476, 524), (539, 593), (538, 695), (598, 763), (626, 626), (701, 696), (785, 771), (784, 629), (858, 691), (931, 764), (924, 597), (1017, 644), (1050, 766), (1124, 678), (1180, 773), (1024, 540), (1047, 379), (1022, 272), (995, 156), (972, 48), (1081, 34), (1118, 127), (883, 180), (855, 56), (766, 161), (728, 38), (653, 163), (606, 31), (540, 195), (451, 272), (340, 251), (267, 331), (211, 422), (115, 353), (8, 300), (189, 261), (12, 201), (11, 104), (112, 185), (126, 78), (222, 75), (242, 169), (318, 100), (385, 159), (507, 100), (425, 36), (306, 2)]

# Number of possible grid locations
STARTING_POSITIONS = len(TOWER_GRID)

# Grid square size
TOWER_GRID_SIZE = 64

# Smaller dark spot when manually placing the towers
GRID_DISPLAY_SIZE = 45

TRAINING_MODE = True    #If true will uncap framerates  TODO  not sure this is used anymore
# VISUAL_MODE = False     #Set false to stop rendering
FPS = 60

#Player
STARTING_COINS   = 500
BUYING_THRESHOLD = 200         # the number of coins to trigger the AI to decide where to buy a new tower

#Spawn Probabilities
GLOBAL_SPAWN_PROB_INC = 0.25   # Percent increase spawn chance per level
ENEMY_PROB_INC = 0.20          # Percent increase number of enemies per level
ENEMY_SPAWN_INC = 0.30         # Increments individual enemies spawn chances

#Level increase constants
# STARTING_LEVEL  = 10
HEALTH_INCREASE = 2                     # how much health is added to enemies when increased
SPEED_INCREASE  = 1                     # how much speed is added to enemies when increased
NUMBER_LEVELS_HEALTH_INCREASE = 2       # how many levels before an enemy health increase
NUMBER_LEVELS_SPEED_INCREASE  = 6       # how many levels before an enemy speed increase

#Window Dimensions
WIN_WIDTH = 1200
WIN_HEIGHT = 800

#Enemies
ENEMY_TYPES   = [Zombie, Dino, Dragon, Robot, Wizard, Warrior, Trump]
ENEMY_INDICES = [0, 1, 2, 3, 4, 5, 6]
Y_MAX_OFFSET  = 35  #yOffset along enemy walking path, causes the enemies to not be walking on same exact line

#Towers
TOWER_TYPES      = [SquareTower, BirdCastle, Igloo, WizardTower, Pyramid, Obelisk]
TOWER_INDICES    = [0, 1, 2, 3, 4, 5]
NUMBER_OF_TOWERS = len(TOWER_TYPES)

#Sounds
BG_MUSIC = ["old_town.mp3"]
