from PIL import Image
import pygame


#C
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)


#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 3
}

ENTITY_HEALTH = {
    'Background': 999,
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

#M

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - VERSUS',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}

#S
SPAWN_TIME = 4000

# 1. Carrega a imagem
img = Image.open('asset/MenuBg.png')
LARGURA, ALTURA = img.size

# Agora você pode usar as variáveis
def get_parameters():
    print(f"A LARGURA é: {LARGURA}px")
    print(f"A ALTURA é: {ALTURA}px")


# get_parameters()

