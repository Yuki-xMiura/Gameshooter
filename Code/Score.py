
from datetime import datetime

import pygame
from pygame import Rect, font, surface, rect

from code.Paraments import LARGURA, ALTURA, C_ORANGE, C_WHITE, C_YELLOW, MENU_OPTION, SCORE_POS
from code.DBProxy import DBProxy
def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"


class Score():
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("asset/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def save(self, menu_option=str, player_score=list[int]):
        db_proxy = DBProxy('DBScore')
        name = ""
        pygame.mixer.music.load('asset/Score.mp3') 
        pygame.mixer.music.play(-1)
        while True:
            if menu_option == MENU_OPTION[0]:
                text = f"Enter your name (5 characters): "
                score = player_score[0]
            elif menu_option == MENU_OPTION[1]:
                text = f"Enter your Team name (5 characters): "
                score = player_score[0] + player_score[1] // 2
            elif menu_option == MENU_OPTION[2]:
                if player_score[0] > player_score[1]:
                    text = f"Player 1 wins! Enter your name (5 characters): "
                    score = player_score[0]
                elif player_score[0] < player_score[1]:
                    text = f"Player 2 wins! Enter your name (5 characters): "
                    score = player_score[1]
                else:
                    text = f"It's a tie! Enter your name (5 characters): "
                    score = max(player_score)
            else:
                return
    
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(text_size=50, text="YOU WIN!", text_color=(C_ORANGE), text_center_pos=SCORE_POS['Title'])
            self.score_text(text_size=20, text=text, text_color=(C_WHITE), text_center_pos=SCORE_POS['EnterName'])
            self.score_text(text_size=20, text=name, text_color=(C_WHITE), text_center_pos=SCORE_POS['Name'])
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_RETURN and 0 < len(name) <= 5:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < 5 and event.unicode.isalnum():
                        name += event.unicode
            pygame.display.flip()


    def show(self,):
        pygame.mixer.music.load('asset/Score.mp3') 
        pygame.mixer.music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(text_size=50, text="TOP 10 SCORES", text_color=(C_ORANGE), text_center_pos=SCORE_POS['Title'])

            for i, (name, score, date) in enumerate(list_score):
                pos = SCORE_POS.get(i, (LARGURA/2, 110 + i*20))
                self.score_text(text_size=20, text=f"{name} - {score} - {date}", text_color=(C_WHITE), text_center_pos=pos)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                # If the event is QUIT then exit the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                        
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)

# score = Score(pygame.display.set_mode(size=(LARGURA,ALTURA)))
# score.show([100, 200])


