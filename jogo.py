# Importa funções auxiliares (níveis, geração de número, mensagens)
import funcoesaux as f

def jogo():
    """
    Função principal do jogo.
    Controla:
    - Número de vidas
    - Tentativas realizadas
    - Comparação entre palpite e número secreto
    """

    vidas = 7                 # Número máximo de tentativas
    numTentativas = 0         # Contador de tentativas feitas

    # Escolha do nível (define intervalo)
    nivel = f.escolha_nivel()

    # Gera número aleatório com base no nível escolhido
    numRandom = f.gerarNumRandom(nivel)

    # DEBUG: Mostra número gerado (ideal remover em versão final)
    print(f"Numero Random: {numRandom}")

    # Ciclo principal do jogo (enquanto houver vidas)
    while vidas > 0:

        # Solicita número ao utilizador
        numEscolhido = int(input(f"{f.escolherNum(nivel)}"))

        # Incrementa contador de tentativas
        numTentativas += 1

        # Caso o jogador acerte
        if numEscolhido == numRandom:
            print(f"Parabéns por ter conseguido acertar no numero!\nNº Tentativas Realizadas: {numTentativas}")
            break

        # Caso o número seja inferior ao secreto
        elif numEscolhido < numRandom:
            print("O numero que escolheu é menor que o numero que o computador gerou automaticamente!")
            vidas -= 1
            print(f"Nº Total de Vidas: {vidas}\nNº Tentativas Realizadas: {numTentativas}")

        # Caso o número seja superior ao secreto
        elif numEscolhido > numRandom:
            print("O numero que escolheu é maior que o numero que o computador gerou automaticamente!")
            vidas -= 1
            print(f"Nº Total de Vidas: {vidas}\nNº Tentativas Realizadas: {numTentativas}")

    # Se ficar sem vidas
    if vidas == 0:
        print(f"O numero que o computador gerou automaticamente foi: {numRandom}\n")
    else:
        # Caso termine por vitória
        pass