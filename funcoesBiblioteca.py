import math as m

def menu():
  operation = int(input("Qual a Operação que deseja fazer?\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potencia\n6 - Raiz Quadrada\n7 - Sair\n> "))
  return operation

def addition(arrayNumbers):
  return f"A Soma de {arrayNumbers[0]} com {arrayNumbers[1]} é igual a {m.fsum(arrayNumbers)}"

def subtraction(firstNumber, secondNumber):
  return f" A Subtração de {firstNumber} com {secondNumber} é igual a {firstNumber - secondNumber}"

def multiplication(firstNumber, secondNumber):
  return f"A Multiplicação de {firstNumber} com {secondNumber} é igual a {firstNumber * secondNumber}"

def division(firstNumber, secondNumber):
  if secondNumber == 0:
    return "Não é possivel dividir por 0"
  else:
    return f"A Divisão de {firstNumber} com {secondNumber} é igual a  {firstNumber / secondNumber}"

def potentiation(firstNumber, secondNumber):
  return f"A Potencia de {firstNumber} com {secondNumber} é igual a {m.pow(firstNumber,secondNumber)}"

def squareroot(number):
  return f"A Raiz Quadrada de {number} é igual a {m.sqrt(number)}"

def ask2numbers():
  firstNumber = float(input("Escreva o primeiro numero: "))
  secondNumber = float(input("Escreva o segundo numero: "))
  
  return (firstNumber, secondNumber)
