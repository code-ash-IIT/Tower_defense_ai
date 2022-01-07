import pygame # importing the pygame module
import os #importing os to set the path to our assets

class Game:
    def __init__(self):
        self.width=1000
        self.height=800
        self.win=pygame.display.set_mode((self.width, self.height))
        self.enemies=[]
        self.towers=[]
        self.lives=10
        self.money=100
        # The line below will make our backgroud image to be loaded and store it in the object
        self.bg=pygame.image.load(os.path.join("assets", "bg.png")) #remember to keep the background image file name same as the one laoded

    def run(self):
        run=True
        # this is to create an object clock to controll the running rate of the while loop
        clock = pygame.time.Clock()
        # we run this loop which means our game is in continuous execution
        while(run):
            # setting our FPS to 60 FPS
            clock.tick(60)
            # we are fetchin the any event of importance 
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    run=False
        
        # to end the program 
        pygame.quit()
    
    def draw(self):
        self.win.blit(self.bg, (0,0))
        pygame.display.update()