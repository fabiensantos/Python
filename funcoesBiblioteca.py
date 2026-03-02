import math as m

def menu():
  operation = int(input("Qual a Operação que deseja fazer?\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potencia\n6 - Raiz Quadrada\n7 - Sair\n> "))
  return operation

def addition(arrayNumbers):
  return m.fsum(arrayNumbers)

def subtraction(firstNumber, secondNumber):
  return firstNumber - secondNumber

def multiplication(firstNumber, secondNumber):
  return firstNumber * secondNumber

def division(firstNumber, secondNumber):
  return firstNumber / secondNumber

def potentiation(firstNumber, secondNumber):
  return m.pow(firstNumber,secondNumber)

def squareroot(number):
  return m.sqrt(number)

def ask2numbers():
  firstNumber = float(input("Escreva o primeiro numero: "))
  secondNumber = float(input("Escreva o segundo numero: "))
  
  return (firstNumber, secondNumber)