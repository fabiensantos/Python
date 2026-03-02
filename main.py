'''
JOGO DA ADIVINHA

Objetivo:
Criar um jogo onde o computador escolhe um número aleatório e o jogador tenta adivinhar.

Requisitos:
- Gerar número aleatório entre limites definidos
- Máximo de 7 tentativas
- Indicar se o palpite é alto, baixo ou correto
- Mostrar tentativas restantes
- Revelar número caso perca
- Permitir jogar novamente
- Implementar níveis de dificuldade

'''

# Importa o módulo principal do jogo
import jogo as j

def menu():
    """
    Função responsável por apresentar o menu principal
    e encaminhar o utilizador conforme a opção escolhida.
    """

    # Apresenta menu e converte input para inteiro
    escolha = int(input(
        "JOGO DA ADIVINHA\n"
        "1 - Começar a Jogar\n"
        "2 - Objetivo do Jogo\n"
        "3 - Sair\n> "
    ))

    # Se escolher iniciar o jogo
    if escolha == 1:
        j.jogo()   # Chama a função principal do jogo
        menu()     # Volta a apresentar o menu após terminar

    # Se escolher ver o objetivo
    elif escolha == 2:
        print("Jogo onde o computador escolhe um número aleatório e o jogador tenta adivinhar")
        menu()     # Reapresenta menu

    # Se escolher sair
    elif escolha == 3:
        print("Obrigado por ter jogado ao Jogo da Adivinha")

# Execução inicial do programa
menu()