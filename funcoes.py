def menu():
  operation = int(input("Qual a Operação que deseja fazer?\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potencia\n6 - Raiz Quadrada\n7 - Sair\n> "))
  return operation

def addition(firstNumber, secondNumber):
  return firstNumber + secondNumber

def subtraction(firstNumber, secondNumber):
  return firstNumber - secondNumber

def multiplication(firstNumber, secondNumber):
  return firstNumber * secondNumber

def division(firstNumber, secondNumber):
  return firstNumber / secondNumber

def potentiation(firstNumber, secondNumber):
  return firstNumber ** secondNumber

def squareroot(number):
  return number ** 0.5

def ask2numbers():
  firstNumber = float(input("Escreva o primeiro numero: "))
  secondNumber = float(input("Escreva o segundo numero: "))
  
  return (firstNumber, secondNumber)