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

from constants.gameConstants import *
from constants.aiConstants import *
from constants.animationConstants import *

pygame.font.init()
pygame.init()

# path = [(5, 318), (53, 346), (113, 401), (172, 414), (227, 366), (276, 284), (320, 284), (383, 292), (434, 247), (492, 214), (550, 206), (611, 216), (668, 246), (706, 303), (724, 354), (717, 375), (682, 428), (638, 455), (589, 471), (540, 472), (487, 463), (496, 419), (507, 378), (531, 347)]

lives_img = pygame.image.load(os.path.join("assets","heart.png")).convert_alpha()
star_img = pygame.image.load(os.path.join("assets","star.png")).convert_alpha()
side_img = pygame.transform.scale(pygame.image.load(os.path.join("assets","side.png")).convert_alpha(), (120, 500))

buy_archer = pygame.transform.scale(pygame.image.load(os.path.join("assets","buy_archer.png")).convert_alpha(), (75, 75))
buy_archer_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets","buy_archer_2.png")).convert_alpha(), (75, 75))
buy_damage = pygame.transform.scale(pygame.image.load(os.path.join("assets","buy_damage.png")).convert_alpha(), (75, 75))
buy_range = pygame.transform.scale(pygame.image.load(os.path.join("assets","buy_range.png")).convert_alpha(), (75, 75))

play_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets","button_start.png")).convert_alpha(), (75, 75))
pause_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets","button_pause.png")).convert_alpha(), (75, 75))

sound_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets","button_sound.png")).convert_alpha(), (75, 75))
sound_btn_off = pygame.transform.scale(pygame.image.load(os.path.join("assets","button_sound_off.png")).convert_alpha(), (75, 75))

wave_bg = pygame.transform.scale(pygame.image.load(os.path.join("assets","wave.png")).convert_alpha(), (225, 75))

attack_tower_names = ["archer", "archer2"]
support_tower_names = ["range", "damage"]

# load music
pygame.mixer.music.load(os.path.join("assets/sound", "song.ogg"))

# waves are in form
# frequency of enemies
# (# mosquitos, # wizards, # clubs, # Zombies)
waves = [
    [3, 3, 3, 3, 3, 3 ,3],
    [10, 10, 10],
    [10, 10, 10],
    [0, 20, 0],
    [0, 50, 0, 1],
    [0, 100, 0],
    [20, 100, 0],
    [50, 100, 0],
    [100, 100, 0],
    [0, 0, 50, 3],
    [20, 0, 100],
    [20, 0, 150],
    [200, 100, 200],
]

class InnerGameRecord:

    def __init__(self):
        self.currentScore = 0
        self.currentLevel = 0
        self.currentEnemiesKilled = 0
        self.currentNumberOfEnemies = 0
        self.currentNumberOfTowers = 0
        self.died = 0
        self.typeOfTowerPlaced = 0
        self.towerX = 0
        self.towerY = 0

        self.currentTowers = []



class Game:
    def __init__(self, win, visualMode, towers, gameRecord, collectInnerGameData):

        self.visualMode           = visualMode
        self.gameRecord           = gameRecord
        self.collectInnerGameData = collectInnerGameData
        self.innerGameRecords     = []
        
        self.width = WIN_WIDTH
        self.height = WIN_HEIGHT
        self.win = win
        self.enemys = []
        self.attack_towers = []
        self.support_towers = []
        self.lives = 10
        self.money = 2000
        self.bg = pygame.image.load(os.path.join("assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.life_font = pygame.font.SysFont("arial", 50)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width - side_img.get_width() + 70, 250, side_img)
        self.menu.add_btn(buy_archer, "buy_archer", 500)
        self.menu.add_btn(buy_archer_2, "buy_archer_2", 500)
        self.menu.add_btn(buy_damage, "buy_damage", 500)
        self.menu.add_btn(buy_range, "buy_range", 500)
        self.moving_object = None
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.pause = True
        self.music_on = True
        self.playPauseButton = PlayPauseButton(play_btn, pause_btn, 10, self.height - 85)
        self.soundButton = PlayPauseButton(sound_btn, sound_btn_off, 90, self.height - 85)

    def gen_enemies(self):
        """
        generate the next enemy or enemies to show
        :return: enemy
        """
        if sum(self.current_wave) == 0:
            if len(self.enemys) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
                self.pause = True
                self.playPauseButton.paused = self.pause
        else:
            wave_enemies = [Mosquito(), Baby_zombie(), Rick(),  Giant(), Club(), Zombie(), Wizard()] #changed position
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemys.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def run(self):
        pygame.mixer.music.play(loops=-1)
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)

            if self.pause == False:
                # gen monsters
                if time.time()-self.timer>=random.randrange(1, 8):
                    self.timer = time.time()
                    self.gen_enemies()

                # # entry point for GAagent for data collection
                # # if self.collectInnerGameData:
                # #     if self.wallet.coins >= BUYING_THRESHOLD and len(self.towers) <= NUMBER_OF_STARTING_TOWERS:
                # #         self.chooseNewTowerRandomly()
                # self.spawnEnemies()
                # self.towerHealthCheck()
                # self.towersAttack()
                # self.enemiesAttack()
                # self.enemiesMove(self.ticks)
                # self.removeEnemies()

                # run = self.isAlive()
                # self.ticks += 1

            pos = pygame.mouse.get_pos()

            # check for moving object
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
                tower_list = self.attack_towers[:] + self.support_towers[:]
                collide = False
                for tower in tower_list:
                    if tower.collide(self.moving_object):
                        collide = True
                        tower.place_color = (255, 0, 0, 100)
                        self.moving_object.place_color = (255, 0, 0, 100)
                    else:
                        tower.place_color = (0, 0, 255, 100)
                        if not collide:
                            self.moving_object.place_color = (0, 0, 255, 100)

            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    # if you're moving an object and click
                    if self.moving_object:
                        not_allowed = False
                        tower_list = self.attack_towers[:] + self.support_towers[:]
                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True

                        if not not_allowed and self.point_to_line(self.moving_object):
                            if self.moving_object.name in attack_tower_names:
                                self.attack_towers.append(self.moving_object)
                            elif self.moving_object.name in support_tower_names:
                                self.support_towers.append(self.moving_object)

                            self.moving_object.moving = False
                            self.moving_object = None

                    else:
                        # check for play or pause
                        if self.playPauseButton.click(pos[0], pos[1]):
                            self.pause = not(self.pause)
                            self.playPauseButton.paused = self.pause

                        if self.soundButton.click(pos[0], pos[1]):
                            self.music_on = not(self.music_on)
                            self.soundButton.paused = self.music_on
                            if self.music_on:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()

                        # look if you click on side menu
                        side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if side_menu_button:
                            cost = self.menu.get_item_cost(side_menu_button)
                            if self.money >= cost:
                                self.money -= cost
                                self.add_tower(side_menu_button)

                        # look if you clicked on attack tower or support tower
                        btn_clicked = None
                        if self.selected_tower:
                            btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            if btn_clicked:
                                if btn_clicked == "Upgrade":
                                    cost = self.selected_tower.get_upgrade_cost()
                                    if self.money >= cost:
                                        self.money -= cost
                                        self.selected_tower.upgrade()

                        if not(btn_clicked):
                            for tw in self.attack_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

                            # look if you clicked on support tower
                            for tw in self.support_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

            # loop through enemies
            if not self.pause:
                to_del = []
                for en in self.enemys:
                    en.move()
                    if en.completed:
                        to_del.append(en)

                # delete all enemies off the screen
                for d in to_del:
                    self.lives -= 1
                    self.enemys.remove(d)

                # loop through attack towers
                for tw in self.attack_towers:
                    self.money += tw.attack(self.enemys)

                # loop through attack towers
                for tw in self.support_towers:
                    tw.support(self.attack_towers)

                # if you lose
                if self.lives <= 0:
                    print("You Lose")
                    run = False

            self.draw()


    def point_to_line(self, tower):
        """
        returns if you can place tower based on distance from
        path
        :param tower: Tower
        :return: Bool
        """
        # find two closest points
        return True

    def draw(self):
        self.win.blit(self.bg, (0,0))

        # draw placement rings
        if self.moving_object:
            for tower in self.attack_towers:
                tower.draw_placement(self.win)

            for tower in self.support_towers:
                tower.draw_placement(self.win)

            self.moving_object.draw_placement(self.win)

        # draw attack towers
        for tw in self.attack_towers:
            tw.draw(self.win)

        # draw support towers
        for tw in self.support_towers:
            tw.draw(self.win)

        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        # redraw selected tower
        if self.selected_tower:
            self.selected_tower.draw(self.win)

        # draw moving object
        if self.moving_object:
            self.moving_object.draw(self.win)

        # draw menu
        self.menu.draw(self.win)

        # draw play pause button
        self.playPauseButton.draw(self.win)

        # draw music toggle button
        self.soundButton.draw(self.win)

        # draw lives
        text = self.life_font.render(str(self.lives), 1, (255,255,255))
        life = pygame.transform.scale(lives_img,(50,50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 13))
        self.win.blit(life, (start_x, 10))

        # draw money
        text = self.life_font.render(str(self.money), 1, (255, 255, 255))
        money = pygame.transform.scale(star_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 75))
        self.win.blit(money, (start_x, 65))

        # draw wave
        self.win.blit(wave_bg, (10,10))
        text = self.life_font.render("Level #" + str(self.wave), 1, (255,255,255))
        self.win.blit(text, (10 + wave_bg.get_width()/2 - text.get_width()/2, 25))

        pygame.display.update()

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_archer", "buy_archer_2", "buy_damage", "buy_range"]
        object_list = [ArcherTower(x,y), ArcherTowerShort(x,y), DamageTower(x,y), RangeTower(x,y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")



    #   # Randomly buys a new tower and places it for data collection
    # def chooseNewTowerRandomly(self):

    #     while True:
    #         towerType = random.randint(0, NUMBER_OF_TOWERS - 1)
    #         towerPlacement = random.randint(0, STARTING_POSITIONS - 1)
    #         if self.towerGrid[towerPlacement][1] == False:
    #             # this will be used to map a tower to its record for data keeping purposes
    #             index = len(self.innerGameRecords)

    #             # place a random tower type in a random position
    #             self.towerGrid[towerPlacement] = ((TOWER_GRID[towerPlacement], True, towerType + 1))
    #             self.placeTower(towerType, TOWER_GRID[towerPlacement], index)

    #             # collect data for record
    #             newRecord = InnerGameRecord()
    #             newRecord.currentScore = self.score
    #             newRecord.currentLevel = self.level
    #             newRecord.currentEnemiesKilled = self.totalEnemiesKilled
    #             newRecord.currentNumberOfEnemies = len(self.enemies)
    #             newRecord.currentNumberOfTowers = len(self.towers)
        #         newRecord.typeOfTowerPlaced = towerType
        #         newRecord.towerX = TOWER_GRID[towerPlacement][0]
        #         newRecord.towerY = TOWER_GRID[towerPlacement][1]

        #         for i in range(STARTING_POSITIONS):
        #             if self.towerGrid[i][1] == False:
        #                 newRecord.currentTowers.append(0)
        #             else:
        #                 # included a digit in tower grids tuples to include tower type
        #                 newRecord.currentTowers.append(self.towerGrid[i][2])

        #         # add new record to the list
        #         self.innerGameRecords.append(newRecord)

        #         break

        # return


        
#     def getReward(self, tower):
#         reward = 0
#         if tower != None:
#             # reward =  tower.damageDealtOnTurn * 3
#             # reward -= tower.damageTakenOnTurn * 2
#             reward += self.score              
#         else:
#             reward += TOWER_POSITION_TAKEN_PENALTY

#         return reward

# TOWER_POSITION_TAKEN_PENALTY = -1000

