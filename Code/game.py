import pygame

from code.Menu import Menu
from code.Paraments import ALTURA, LARGURA, MENU_OPTION, ENTITY_HEALTH
from code.Level import Level
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(LARGURA,ALTURA))
        

    def run(self, ):

        while True:
            score = Score(self.window)
            menu = Menu(self.window)

            
            menu_return = menu.run()
            player_score = [0, 0]
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                print("Iniciando jogo")
                player_health = [ENTITY_HEALTH['Player1'], ENTITY_HEALTH['Player2']]
                level = Level(self.window, name='Level1', game_mode=menu_return, player_score=player_score, player_health=player_health)
                level_return = level.run(player_score, player_health)
                if level_return:
                    level = Level(self.window, name='Level2', game_mode=menu_return, player_score=player_score, player_health=player_health)
                    level.run(player_score, player_health)
                    if level_return:
                        score.save(menu_return, player_score)
            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                print("Saindo do jogo")
                pygame.quit()
                exit()
            pass
        
        # Check for all events

            for event in pygame.event.get():
                # If the event is QUIT then exit the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    #teste