from Tower_defense import Game
from ai import AIplay
from geneticAlgorithm.parallelGA import ParallelGeneticAlgorithm
from geneticAlgorithm.serialGA import SerialGeneticAlgorithm

from enum import Enum
import pygame
import os

start_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets", "button_play.png")).convert_alpha(),(150,150))
logo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "logo.png")).convert_alpha(),(900,350))
ai_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets", "ai.png")).convert_alpha(),(150,150))

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


class MainMenu:
    def __init__(self, win):
        self.width = 900
        self.height = 674
        self.bg = pygame.image.load(os.path.join("assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win
        self.btn = (self.width/2 - start_btn.get_width()/2, 350, start_btn.get_width(), start_btn.get_height())
        self.ai_b = (self.width/2 - ai_btn.get_width()/2, 500, ai_btn.get_width(), ai_btn.get_height())

    


    


    # # the game expects the following signature:
    # #      Game(visualMode, towers, gameRecord, collectInnerGameData, deepQagent)

    # def main():
    #     ''' Entry point for game '''

    #     #Setup Game
    #     pygame.init()
    #     pygame.font.init()
    #     pygame.mixer.init()
    #     pygame.display.set_caption("AI Tower Defense")

    #     # displaySettings()

    #     # Determine game mode
    #     if GAME_MODE == MODE.manual:
    #         game = Game(True, [], None, False, None)
    #         game.run()
    #     elif GAME_MODE == MODE.geneticAlgorithm:
    #         if PARALLEL_MODE:
    #             gaAlgo = ParallelGeneticAlgorithm(VISUAL_MODE, READ_FILE, SAVE_TO_DISK, PRINT_GRAPHS, COLLECT_WHOLE_GAME_DATA, COLLECT_INNER_GAME_DATA)
    #         else:
    #             gaAlgo = SerialGeneticAlgorithm(VISUAL_MODE, READ_FILE, SAVE_TO_DISK, PRINT_GRAPHS, COLLECT_WHOLE_GAME_DATA, COLLECT_INNER_GAME_DATA)
    #         gaAlgo.run()

    #     pygame.quit()

    # def displaySettings():
    #     ''' Displays the current game settings '''
    #     print(f"\n=== AI Tower Defense Settings ===")
    #     print(f"Game Mode:              {GAME_MODE.name}")
    #     # if GAME_MODE.name == "qLearning":
    #         # print(f"Training Mode:          {Q_TRAINING_MODE}")
    #     print(f"Parallel Mode:          {PARALLEL_MODE}")
    #     print(f"Visual Mode:            {VISUAL_MODE}")
    #     print(f"Load model from file:   {READ_FILE}")
    #     print(f"Save model to file:     {SAVE_TO_DISK}")
    #     print(f"Save graphs:            {PRINT_GRAPHS}\n")


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


