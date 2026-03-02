# 🇵🇹 

# 🎯 Jogo da Adivinha 

---

## 📌 Objetivo de Aprendizagem

Este projeto tem como principal objetivo consolidar os seguintes conceitos fundamentais de programação em Python:

- Organização de código em múltiplos ficheiros
- Separação de responsabilidades (modularização)
- Utilização de funções
- Estruturas de controlo (`if/elif/else`, `while`)
- Manipulação de input do utilizador
- Geração de números aleatórios
- Implementação de lógica condicional
- Controlo de fluxo e gestão de tentativas
- Estruturação de um menu interativo

O projeto também introduz o conceito de **níveis de dificuldade**, reforçando a adaptação dinâmica de lógica com base em parâmetros.

---

## 📂 Conteúdo de Cada Ficheiro

### 🔹 <a href="https://github.com/fabiensantos/Python/blob/jogo_adivinha/main.py">`main.py`</a>

Responsável pela gestão do menu principal.

Contém:
- Apresentação do menu interativo
- Encaminhamento para a execução do jogo
- Exibição do objetivo do jogo
- Controlo de saída do programa

É o ponto de entrada da aplicação.

---

### 🔹 <a href="https://github.com/fabiensantos/Python/blob/jogo_adivinha/jogo.py">`jogo.py`</a>

Contém a lógica principal do jogo.

Responsabilidades:
- Definição do número de vidas
- Controlo das tentativas
- Comparação entre o número escolhido e o número secreto
- Indicação se o palpite é:
  - Maior
  - Menor
  - Correto
- Gestão de fim de jogo (vitória ou derrota)

Implementa o ciclo principal `while` que controla o estado do jogo.

---

### 🔹 <a href="https://github.com/fabiensantos/Python/blob/jogo_adivinha/funcoesaux.py">`funcoesaux.py`</a>

Módulo auxiliar com funções de suporte.

Inclui:
- Escolha do nível de dificuldade
- Geração do número aleatório com base no nível
- Mensagem dinâmica para pedido de número ao utilizador

Separa a lógica auxiliar da lógica principal, promovendo melhor organização e legibilidade.

---

## 📚 Bibliotecas Utilizadas

| Biblioteca | Utilização |
|------------|------------|
| `random`   | Geração de números aleatórios |

Importação:
```python
import random as r
```

# 🇬🇧

# 🎯 Number Guessing Game

---

## 📌 Learning Objectives

This project aims to consolidate fundamental Python programming concepts, including:

- Code organisation across multiple files
- Separation of concerns (modular design)
- Function implementation
- Control flow structures (`if/elif/else`, `while`)
- User input handling
- Random number generation
- Conditional logic implementation
- Attempt tracking and game state control
- Interactive menu structure

The project also introduces **difficulty levels**, reinforcing dynamic logic adjustment based on parameters.

---

## 📂 File Structure and Responsibilities

### 🔹 <a href="https://github.com/fabiensantos/Python/blob/jogo_adivinha/main.py">`main.py`</a>

Responsible for managing the main menu.

Contains:
- Interactive menu presentation
- Redirection to game execution
- Display of the game objective
- Exit control

This is the application entry point.

---

### 🔹 <a href="https://github.com/fabiensantos/Python/blob/jogo_adivinha/jogo.py">`jogo.py`</a>

Contains the core game logic.

Responsibilities:
- Defining the number of lives
- Tracking attempts
- Comparing the user’s guess with the secret number
- Informing whether the guess is:
  - Too high
  - Too low
  - Correct
- Managing end-game scenarios (win or loss)

Implements the main `while` loop that controls the game state.

---

### 🔹 <a href="https://github.com/fabiensantos/Python/blob/jogo_adivinha/funcoesaux.py">`funcoesaux.py`</a>

Auxiliary module containing supporting functions.

Includes:
- Difficulty level selection
- Random number generation based on selected level
- Dynamic user prompt according to difficulty range

Separates supporting logic from the core gameplay logic, improving organisation and readability.

---

## 📚 Libraries Used

| Library   | Purpose |
|-----------|---------|
| `random`  | Random number generation |

Import:
```python
import random as r
```
