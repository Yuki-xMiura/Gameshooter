#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from code.Enemy import Enemy
from code.Player import Player
from code.Background import Background
from code.Paraments import ALTURA, LARGURA

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0,0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(LARGURA,0)))
                return list_bg
            case 'Player1':
                return Player(name='Player1', position=(10, ALTURA/2))
            case 'Player2':
                return Player(name='Player2', position=(10, ALTURA/2 - 50))
            case 'Enemy1':
                return Enemy(name='Enemy1', position=(LARGURA, random.randint(40, ALTURA-40)))
            case 'Enemy2':
                return Enemy(name='Enemy2', position=(LARGURA, random.randint(40, ALTURA-40)))
