from PIL import Image


#C
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)

#M
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

