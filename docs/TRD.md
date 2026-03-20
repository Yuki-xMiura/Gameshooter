# Technical Requirements Document (TRD)

## Visão Geral Técnica

**Nome do Projeto:** GameShooter  
**Versão:** 1.0  
**Data:** 25 de fevereiro de 2026  
**Autor:** Yukim  

Este documento descreve os requisitos técnicos, arquitetura e estrutura do projeto GameShooter, um jogo de tiro desenvolvido em Python com Pygame.

## Arquitetura do Sistema

### Visão Geral da Arquitetura
O projeto segue uma arquitetura orientada a objetos simples, utilizando Pygame para renderização gráfica e manipulação de eventos. O código é modularizado em classes separadas para entidades, níveis, menus e fábricas.

- **Linguagem Principal:** Python 3.13
- **Framework Gráfico:** Pygame
- **Biblioteca de Imagens:** PIL (Pillow)
- **Padrão Arquitetural:** MVC-like (Model-View-Controller) com separação entre lógica de jogo, entidades e interface.

### Componentes Principais
- **Game:** Classe principal que gerencia o loop do jogo e transições entre menu e níveis.
- **Menu:** Gerencia a interface do menu principal.
- **Level:** Gerencia a lógica de um nível específico, incluindo entidades e eventos.
- **Entity:** Classe base para todas as entidades do jogo (jogadores, inimigos, backgrounds).
- **EntityFactory:** Fábrica para criação de entidades.
- **Paraments:** Módulo com constantes e configurações globais.

## Estrutura de Pastas

A estrutura de pastas do projeto é organizada da seguinte forma:

```
Gameshooter/
├── main.py                 # Ponto de entrada do jogo
├── requirements.txt        # Dependências do projeto
├── asset/                  # Recursos gráficos e de áudio
│   ├── MenuBg.png         # Fundo do menu
│   └── level1.mp3         # Música do nível 1
├── code/                   # Código fonte principal
│   ├── __init__.py        # Inicialização do módulo
│   ├── Background.py      # Lógica de backgrounds
│   ├── Enemy.py           # Lógica de inimigos
│   ├── Entity.py          # Classe base para entidades
│   ├── EntityFactory.py   # Fábrica de entidades
│   ├── Game.py            # Classe principal do jogo
│   ├── Level.py           # Lógica de níveis
│   ├── Menu.py            # Lógica do menu
│   ├── Paraments.py       # Constantes e parâmetros
│   ├── Player.py          # Lógica do jogador
│   └── __pycache__/       # Cache de bytecode Python
└── docs/                   # Documentação
    ├── PRD.md             # Product Requirements Document
    └── TRD.md             # Technical Requirements Document
```

### Descrição das Pastas
- **Raiz (/):** Contém arquivos principais como `main.py` e `requirements.txt`.
- **asset/:** Armazena todos os recursos estáticos (imagens, sons, músicas).
- **code/:** Contém todo o código fonte Python, organizado em módulos.
- **docs/:** Documentação do projeto, incluindo PRD e TRD.

## Requisitos Técnicos Detalhados

### Ambiente de Desenvolvimento
- **Sistema Operacional:** Windows (compatível com outras plataformas via Pygame)
- **Python:** Versão 3.13 ou superior
- **IDE:** Qualquer editor que suporte Python (recomendado: VS Code)

### Dependências
- **pygame:** Biblioteca principal para jogos 2D
  - Versão: 2.x
  - Instalação: `pip install pygame`
- **pillow (PIL):** Para manipulação de imagens
  - Versão: 10.x
  - Instalação: `pip install pillow`

### Configurações de Hardware
- **CPU:** Qualquer processador moderno
- **RAM:** Mínimo 512 MB
- **GPU:** Suporte básico a OpenGL
- **Armazenamento:** 50 MB para instalação + espaço para assets

### Configurações de Software
- **Resolução:** Dinâmica, baseada no tamanho da imagem de fundo do menu
- **FPS:** 60 quadros por segundo
- **Controles:** Teclado (setas para Player1, WASD para Player2)

## Padrões de Codificação

### Convenções de Nomenclatura
- **Classes:** PascalCase (ex: `Entity`, `Game`)
- **Funções/Métodos:** snake_case (ex: `get_entity`, `run`)
- **Variáveis:** snake_case (ex: `entity_list`, `window`)
- **Constantes:** UPPER_CASE (ex: `LARGURA`, `MENU_OPTION`)

### Estrutura de Código
- Uso de classes para encapsulamento
- Herança para entidades (Entity como classe base)
- Fábrica para criação de objetos (EntityFactory)
- Constantes centralizadas em Paraments.py

## Protocolos de Comunicação

### Eventos do Jogo
- **EVENT_ENEMY:** Evento customizado para spawn de inimigos (intervalo: 4000ms)
- **pygame.USEREVENT:** Base para eventos customizados

### Entrada do Usuário
- **Teclado:** Mapeamento definido em Paraments.py
  - Player1: Setas direcionais
  - Player2: WASD

## Segurança e Performance

### Considerações de Segurança
- O jogo roda localmente, sem conexões de rede
- Validação básica de entrada (eventos Pygame)

### Otimizações de Performance
- Loop principal limitado a 60 FPS
- Renderização eficiente com `blit`
- Gerenciamento de memória para entidades

## Testes e Qualidade

### Estratégia de Testes
- Testes manuais para funcionalidades principais
- Validação de compatibilidade com diferentes versões Python/Pygame

### Métricas de Qualidade
- Código modular e legível
- Documentação em português
- Uso de type hints onde aplicável

## Manutenção e Suporte

### Logs e Debugging
- Print statements para debug básico
- Possibilidade de expansão para logging estruturado

### Versionamento
- Git para controle de versão
- Branches para desenvolvimento de features

## Conclusão

Esta TRD fornece uma visão completa dos aspectos técnicos do projeto GameShooter. A estrutura modular facilita manutenção e expansões futuras, como adição de novos níveis, modos de jogo e recursos.
