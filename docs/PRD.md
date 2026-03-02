# Product Requirements Document (PRD)

## Visão Geral do Produto

**Nome do Produto:** GameShooter
**Versão:** 1.0
**Data:** 25 de fevereiro de 2026
**Autor:** Yukim

GameShooter é um jogo de tiro desenvolvido em Python utilizando a biblioteca Pygame. O jogo oferece uma experiência de jogo clássica de nave espacial com elementos de tiro, inimigos e power-ups, suportando modos single-player e multiplayer cooperativo/versus.

## Objetivos

- Fornecer uma experiência de jogo divertida e envolvente baseada em jogos de tiro clássicos.
- Suportar múltiplos modos de jogo: single-player, cooperativo e versus.
- Implementar mecânicas básicas de jogo como movimento, tiro, colisões e pontuação.
- Criar uma interface de menu intuitiva para navegação.
- Garantir compatibilidade com Windows e facilidade de execução.

## Funcionalidades Principais

### 1. Menu Principal

- Opções de menu:
  - Novo Jogo 1 Jogador
  - Novo Jogo 2 Jogadores - Cooperativo
  - Novo Jogo 2 Jogadores - Versus
  - Placar (Score)
  - Sair
- Fundo de menu personalizado carregado de assets.

### 2. Modos de Jogo

- **Single-Player:** Um jogador controla uma nave contra inimigos.
- **Cooperativo:** Dois jogadores trabalham juntos contra inimigos.
- **Versus:** Dois jogadores competem um contra o outro (a ser implementado).

### 3. Mecânicas de Jogo

- **Movimento:** Jogadores podem mover suas naves para cima, baixo, esquerda e direita.
- **Tiro:** Jogadores podem atirar projéteis.
- **Inimigos:** Inimigos aparecem periodicamente e se movem em padrões definidos.
- **Colisões:** Detecção de colisões entre projéteis, jogadores e inimigos.
- **Pontuação:** Sistema de pontuação baseado em inimigos derrotados.
- **Backgrounds:** Múltiplas camadas de background com movimento parallax.

### 4. Assets e Recursos

- Imagens para menu, jogadores, inimigos e backgrounds.
- Música de fundo para níveis.
- Sons para efeitos (a ser implementado).

### 5. Sistema de Níveis

- Nível inicial: "level1" com inimigos básicos.
- Possibilidade de expansão para múltiplos níveis.

## Requisitos Técnicos

### Plataforma

- Sistema Operacional: Windows
- Linguagem: Python 3.x
- Bibliotecas: Pygame, PIL (Pillow)

### Dependências

- pygame
- pillow

### Hardware Mínimo

- Processador: Qualquer CPU moderna
- Memória RAM: 512 MB
- Armazenamento: 50 MB
- Placa de Vídeo: Suporte a OpenGL básico

### Resolução

- Resolução padrão: Baseada no tamanho da imagem de fundo do menu (carregada dinamicamente via PIL)

## Requisitos Funcionais

1. O jogo deve iniciar com um menu principal.
2. O jogador deve poder selecionar modos de jogo.
3. No modo de jogo, o jogador deve controlar uma nave com teclado.
4. Inimigos devem aparecer automaticamente em intervalos regulares.
5. Deve haver detecção de colisões entre entidades.
6. O jogo deve ter música de fundo.
7. Deve ser possível sair do jogo a qualquer momento.

## Requisitos Não-Funcionais

- **Performance:** O jogo deve rodar a 60 FPS.
- **Usabilidade:** Interface intuitiva, controles simples.
- **Manutenibilidade:** Código modular com classes separadas para entidades, níveis, etc.
- **Portabilidade:** Compatível com Windows, fácil de instalar via pip.

## Histórias de Usuário

1. Como jogador, quero ver um menu ao iniciar o jogo para escolher o modo de jogo.
2. Como jogador single-player, quero controlar uma nave e atirar em inimigos.
3. Como jogador cooperativo, quero jogar com um amigo contra inimigos.
4. Como jogador, quero ouvir música durante o jogo.
5. Como jogador, quero ver minha pontuação ao final do jogo.

## Critérios de Aceitação

- O menu deve exibir todas as opções corretamente.
- O jogo deve iniciar sem erros em Windows.
- Controles devem responder adequadamente.
- Inimigos devem aparecer e se mover.
- Música deve tocar em loop.

## Riscos e Mitigações

- **Risco:** Dependência de Pygame pode causar problemas de instalação.

  - **Mitigação:** Incluir instruções claras de instalação e requirements.txt.
- **Risco:** Performance em máquinas antigas.

  - **Mitigação:** Otimizar código e reduzir resolução se necessário.

## Roadmap

- **Versão 1.0:** Implementação básica com menu, nível 1 e modos single/cooperativo.
- **Versão 1.1:** Adicionar modo versus, mais níveis, sons.
- **Versão 2.0:** Multiplayer online, mais assets.

## Conclusão

Este PRD define os requisitos para o desenvolvimento inicial do GameShooter. O foco está em criar uma base sólida para um jogo de tiro clássico, com espaço para expansões futuras.
