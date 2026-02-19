from PIL import Image


#C
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)

#M

#E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
}
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - VERSUS',
               'SCORE',
               'EXIT')


# 1. Carrega a imagem
img = Image.open('asset/MenuBg.png')
LARGURA, ALTURA = img.size

# Agora você pode usar as variáveis
def get_parameters():
    print(f"A LARGURA é: {LARGURA}px")
    print(f"A ALTURA é: {ALTURA}px")


# get_parameters()

