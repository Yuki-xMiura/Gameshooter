import pygame

from Code.Menu import Menu
from Code.Paraments import ALTURA, LARGURA

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(LARGURA,ALTURA))

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass
        
        # # Check for all events

        #     for event in pygame.event.get():
        #         # If the event is QUIT then exit the program
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             exit()
        #             #teste