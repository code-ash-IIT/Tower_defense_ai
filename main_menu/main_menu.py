from game import Game
import pygame
import os

start_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets", "button_play.png")).convert_alpha(),(150,150))
logo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "logo.png")).convert_alpha(),(900,350))

class MainMenu:
    def __init__(self, win):
        self.width = 900
        self.height = 674
        self.bg = pygame.image.load(os.path.join("assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win
        self.btn = (self.width/2 - start_btn.get_width()/2, 350, start_btn.get_width(), start_btn.get_height())

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    # check if hit start btn
                    x, y = pygame.mouse.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = Game(self.win)
                            game.run()
                            del game
            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        self.win.blit(logo, (self.width/2 - logo.get_width()/2, 0))
        self.win.blit(start_btn, (self.btn[0], self.btn[1]))
        pygame.display.update()


