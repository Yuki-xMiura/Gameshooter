# GameShooter

## Descrição

GameShooter é um jogo de tiro desenvolvido em Python utilizando a biblioteca Pygame. O jogo oferece uma experiência clássica de nave espacial com elementos de tiro, inimigos e power-ups, suportando modos single-player e multiplayer cooperativo/versus.

## Funcionalidades Principais

- **Menu Principal**: Navegação intuitiva com opções para diferentes modos de jogo.
- **Modos de Jogo**:
  - Single-Player: Um jogador contra inimigos.
  - Cooperativo: Dois jogadores trabalhando juntos.
  - Versus: Dois jogadores competindo (a ser implementado).
- **Mecânicas de Jogo**:
  - Movimento de naves.
  - Sistema de tiro.
  - Detecção de colisões.
  - Pontuação baseada em inimigos derrotados.
  - Backgrounds com movimento parallax.
- **Sistema de Níveis**: Nível inicial com inimigos básicos.

## Requisitos

- **Python**: Versão 3.13 ou superior.
- **Bibliotecas**:
  - pygame==2.6.1
  - pillow==12.1.1
- **Sistema Operacional**: Windows (compatível com outras plataformas via Pygame).

## Instalação

1. Clone ou baixe o repositório do projeto.
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Certifique-se de que a pasta `asset/` contém os recursos necessários (imagens, músicas, etc.).

## Como Jogar

1. Execute o jogo:
   ```
   python main.py
   ```
2. No menu principal, selecione o modo de jogo desejado.
3. Use os controles para mover e atirar.

### Controles

- **Jogador 1**:
  - Movimento: Setas do teclado (↑ ↓ ← →)
  - Tiro: Barra de espaço
- **Jogador 2** (modo cooperativo/versus):
  - Movimento: WASD
  - Tiro: Shift esquerdo

## Estrutura do Projeto

```
Gameshooter/
├── main.py                 # Ponto de entrada do jogo
├── requirements.txt        # Dependências do projeto
├── asset/                  # Recursos gráficos e de áudio
├── code/                   # Código fonte principal
│   ├── Background.py       # Lógica de backgrounds
│   ├── Enemy.py            # Lógica de inimigos
│   ├── Entity.py           # Classe base para entidades
│   ├── EntityFactory.py    # Fábrica de entidades
│   ├── Game.py             # Classe principal do jogo
│   ├── Level.py            # Lógica de níveis
│   ├── Menu.py             # Lógica do menu
│   ├── Paraments.py        # Constantes e parâmetros
│   └── Player.py           # Lógica do jogador
└── docs/                   # Documentação
    ├── PRD.md             # Product Requirements Document
    └── TRD.md             # Technical Requirements Document
```

## Desenvolvimento

O projeto segue uma arquitetura orientada a objetos com separação modular. Para contribuir ou modificar:

- Use classes para encapsulamento.
- Siga convenções de nomenclatura: PascalCase para classes, snake_case para funções/variáveis.
- Teste mudanças no loop principal do jogo.

## Licença

Este projeto é para fins educacionais. Consulte os documentos em `docs/` para mais detalhes sobre requisitos e arquitetura.