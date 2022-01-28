from Tower_defense import Game
from ai import AIplay
import pygame
import os

start_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets", "button_play.png")).convert_alpha(),(150,150))
logo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "logo.png")).convert_alpha(),(900,350))
ai_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets", "ai.png")).convert_alpha(),(150,150))

class MainMenu:
    def __init__(self, win):
        self.width = 900
        self.height = 674
        self.bg = pygame.image.load(os.path.join("assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win
        self.btn = (self.width/2 - start_btn.get_width()/2, 350, start_btn.get_width(), start_btn.get_height())
        self.ai_b = (self.width/2 - ai_btn.get_width()/2, 500, ai_btn.get_width(), ai_btn.get_height())

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
                    if self.ai_b[0] <= x <= self.ai_b[0] + self.ai_b[2]:
                        if self.ai_b[1] <= y <= self.ai_b[1] + self.ai_b[3]:
                            AIplay(self.win)
                            # AIplay.g_run()
            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        self.win.blit(logo, (self.width/2 - logo.get_width()/2, 0))
        self.win.blit(start_btn, (self.btn[0], self.btn[1]))
        self.win.blit(ai_btn, (self.ai_b[0], self.ai_b[1]))
        pygame.display.update()


