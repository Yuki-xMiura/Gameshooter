#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.Paraments import ENTITY_SHOT_COOLDOWN, LARGURA, ENTITY_SPEED   
from code.EnemyShot import EnemyShot

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_cooldown = ENTITY_SHOT_COOLDOWN[self.name]


    def move(self, ):
        self.rect.centerx -= self.speed

    def shot(self,):
        self.shot_cooldown -= 1000 / 60
        if self.shot_cooldown <= 0:
            self.shot_cooldown = ENTITY_SHOT_COOLDOWN[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=self.rect.center )