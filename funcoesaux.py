# Importa módulo random com alias 'r'
import random as r


def escolha_nivel():
    """
    Permite ao utilizador escolher o nível de dificuldade.
    Retorna:
        1 - Fácil (1 a 50)
        2 - Médio (1 a 100)
        3 - Difícil (1 a 500)
    """

    nivel = int(input(
        "Que nivel pretende:\n"
        "1 - Fácil [1 - 50]\n"
        "2 - Médio [1 - 100]\n"
        "3 - Dificil [1 - 500]\n> "
    ))

    if nivel == 1:
        return 1
    elif nivel == 2:
        return 2
    elif nivel == 3:
        return 3
    else:
        print("A opção que escolheu não está disponível. Tente novamente!")
        return escolha_nivel()


def gerarNumRandom(nivel):
    """
    Gera número aleatório com base no nível selecionado.
    Utiliza randrange(inicio, fim, passo)
    """

    if nivel == 1:
        return r.randrange(0, 51, 1)
    elif nivel == 2:
        return r.randrange(0, 101, 1)
    elif nivel == 3:
        return r.randrange(0, 501, 1)


def escolherNum(nivel):
    """
    Retorna mensagem adequada ao intervalo do nível escolhido.
    """

    if nivel == 1:
        return "Escolha um numero entre 1 e 50 (incluidos): "
    elif nivel == 2:
        return "Escolha um numero entre 1 e 100 (incluidos): "
    elif nivel == 3:
        return "Escolha um numero entre 1 e 500 (incluidos): "