#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity
from code.Paraments import MENU_OPTION, ALTURA, LARGURA, C_WHITE, PLAYER_KEY_SHOT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, ENTITY_SHOT_COOLDOWN
from code.PlayerShot import PlayerShot
from code.EnemyShot import EnemyShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_cooldown = 0

    def move(self, ):
        keys = pygame.key.get_pressed()
        if keys[PLAYER_KEY_DOWN[self.name]]:
            self.rect.centery += self.speed
        if keys[PLAYER_KEY_UP[self.name]]:
            self.rect.centery -= self.speed
        if keys[PLAYER_KEY_LEFT[self.name]]:
            self.rect.centerx -= self.speed
        if keys[PLAYER_KEY_RIGHT[self.name]]:
            self.rect.centerx += self.speed
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= ALTURA:
            self.rect.bottom = ALTURA
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= LARGURA:
            self.rect.right = LARGURA
    
    def shot(self,):
        self.shot_cooldown -= 1000 / 60
        if self.shot_cooldown <= 0:
            if pygame.key.get_pressed()[PLAYER_KEY_SHOT[self.name]]:
                self.shot_cooldown = ENTITY_SHOT_COOLDOWN[self.name]
                return PlayerShot(name=f'{self.name}Shot', position=self.rect.center )
                self.shot_cooldown = ENTITY_SHOT_COOLDOWN[self.name]
        

            