import pygame

from code.Menu import Menu
from code.Paraments import ALTURA, LARGURA, MENU_OPTION
from code.Level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(LARGURA,ALTURA))

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                print("Iniciando jogo")
                level = Level(self.window, name='level1', game_mode=menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[3]:
                print("Exibindo placar")
            elif menu_return == MENU_OPTION[4]:
                print("Saindo do jogo")
                pygame.quit()
                exit()
            pass
        
        # # Check for all events

        #     for event in pygame.event.get():
        #         # If the event is QUIT then exit the program
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             exit()
        #             #teste