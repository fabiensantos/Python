'''
1. Calculadora Simples

Objetivo: Criar uma calculadora que realize operações matemáticas básicas.

Requisitos:

- O programa deve apresentar um menu com as opções: 1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão, 5-Sair
- Solicitar ao usuário que escolha uma operação
- Pedir dois números ao usuário
- Realizar a operação escolhida e mostrar o resultado
- Tratar o caso de divisão por zero (mostrar mensagem de erro)
- Após cada operação, perguntar se o usuário deseja realizar outra operação
- O programa só deve terminar quando o usuário escolher a opção "Sair"

Desafio extra: Adicionar operações de potência e raiz quadrada

'''
import funcoes as f

while (True):
  operation = f.menu()
  
  if operation == 1:
    firstNumber, secondNumber = f.ask2numbers()
    print(f"A Soma de {firstNumber} com {secondNumber} é igual a {f.addition(firstNumber,secondNumber)}")
  elif operation == 2:
    firstNumber, secondNumber = f.ask2numbers()
    print(f"A Subtração de {firstNumber} com {secondNumber} é igual a {f.subtraction(firstNumber,secondNumber)}")
  elif operation == 3:
    firstNumber, secondNumber = f.ask2numbers()
    print(f"A Multiplicação de {firstNumber} com {secondNumber} é igual a {f.multiplication(firstNumber,secondNumber)}")
  elif operation == 4:
    firstNumber, secondNumber = f.ask2numbers()
    print(f"A Divisão de {firstNumber} com {secondNumber} é igual a {f.division(firstNumber,secondNumber)}")
  elif operation == 5:
    firstNumber, secondNumber = f.ask2numbers()
    print(f"A Potencia de {firstNumber} com {secondNumber} é igual a {f.potentiation(firstNumber,secondNumber)}")
  elif operation == 6:
    number = float(input("Escreva o numero que deseja fazer a Raiz Quadrada: "))
    print(f"A Raiz Quadrada de {number} é igual a {f.squareroot(number)}")
  elif operation == 7:
    break
  else:
    print("O numero que escolheu não existe, tente novamente!")
