import pygame # importing the pygame module
import time
import random
import os #importing os to set the path to our assets
from enemy.mosquito import Mosquito
from enemy.rick import Rick
from enemy.giant import Giant
from enemy.baby_zombie import Baby_zombie
from towers.archerTower import ArcherTower, Canon

class Game:
    def __init__(self):
        self.width=900
        self.height=674
        self.win=pygame.display.set_mode((self.width, self.height))
        self.enemies=[Mosquito()]
        self.towers=[ArcherTower(310, 320), Canon(550, 400)]   # in the brackets are the positions(x, y)
        self.lives=10
        self.money=100
        # The line below will make our backgroud image to be loaded and store it in the object
        self.bg=pygame.image.load(os.path.join("assets", "bg.png")) #remember to keep the background image file name same as the one laoded
        # self.clicks=[]
        self.timer=time.time()

    def run(self):
        run=True
        # this is to create an object clock to controll the running rate of the while loop
        clock = pygame.time.Clock()
        # we run this loop which means our game is in continuous execution
        while(run):
            if(time.time()-self.timer>=random.randrange(1, 15)):
                self.timer=time.time()
                self.enemies.append(random.choice([Mosquito(), Rick(), Giant(), Baby_zombie()]))
            
            # setting our FPS to 60 FPS
            clock.tick(60)
            # we are fetchin the any event of importance 
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    run=False

                # pos=pygame.mouse.get_pos()
                # if(event.type==pygame.MOUSEBUTTONDOWN):
                #     pass

            self.draw() #calling our draw method in the run method

        # to end the program 
        pygame.quit()
    
    def draw(self):
        self.win.blit(self.bg, (0,0))
        # used it to know the position of the paths
        # for p in self.clicks:
        # pygame.draw.circle(self.win, (255,0,0), (p[0],p[1]), 5)
        # draw enemies

        # draw enemies
        for en in self.enemies:
            en.draw(self.win)
            if(en.completed):
                self.enemies.remove(en)
                
        # draw towers
        for tw in self.towers:
            tw.draw(self.win)

        # loop through towers
        for tw in self.towers:
            tw.attack(self.enemies)

        pygame.display.update()

G_Obj=Game()
G_Obj.run()