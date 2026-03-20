#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import font, surface, rect
from code.Paraments import ALTURA, LARGURA, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("asset/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect()
        
    def run(self,):
        menu_option = 0
        pygame.mixer.music.load('asset/Menu.mp3') 
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Mountain", text_color=(255, 128, 0), text_center_pos=(LARGURA/2, 70))
            self.menu_text(text_size=50, text="Shooter", text_color=(C_ORANGE), text_center_pos=(LARGURA/2, 120))
            
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=(C_YELLOW), text_center_pos=(LARGURA/2, 170 + i*30))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=(C_WHITE), text_center_pos=(LARGURA/2, 170 + i*30))
            pygame.display.flip()


        # Check for all events

            for event in pygame.event.get():
                # If the event is QUIT then exit the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    #teste
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option += 1
                        if menu_option > len(MENU_OPTION) - 1:
                            menu_option = 0
                    elif event.key == pygame.K_UP:
                        menu_option -= 1
                        if menu_option < 0:
                            menu_option = len(MENU_OPTION) - 1
                    elif event.key == pygame.K_RETURN:
                        print(menu_option)
                        return MENU_OPTION[menu_option]
                    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)
            