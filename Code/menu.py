#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import font, surface, rect
from code.Paraments import ALTURA, LARGURA, C_ORANGE, MENU_OPTION, C_WHITE

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("asset/MenuBg.png")
        self.rect = self.surf.get_rect()
        
    def run(self,):
        pygame.mixer.music.load('asset/Menu.mp3') 
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Mountain", text_color=(255, 128, 0), text_center_pos=(LARGURA/2, 70))
            self.menu_text(text_size=50, text="Shooter", text_color=(C_ORANGE), text_center_pos=(LARGURA/2, 120))
            
            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=(C_WHITE), text_center_pos=(LARGURA/2, 170 + i*30))
            pygame.display.flip()


        # Check for all events

            for event in pygame.event.get():
                # If the event is QUIT then exit the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    #teste
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)