#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

import pygame
from code.Paraments import ENTITY_HEALTH, ENTITY_SPEED


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED[self.name]
        self.health = ENTITY_HEALTH[self.name]
    
    @abstractmethod
    def move(self,):
        pass