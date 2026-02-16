#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 600))

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