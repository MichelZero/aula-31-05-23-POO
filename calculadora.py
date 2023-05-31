#
# autores: Michel
#
# data: 24/05/2023

# Exercício 1: crie uma classe que seja uma calculadora, com as operações de soma, subtração, multiplicação e divisão.
# teste a classe

# definindo a classe Calculadora()
class Calculadora():
  # definindo os métodos da classe
  # método somar()
  def somar(self, valor1, valor2):
    total = valor1 + valor2
    return total
  
  # método multiplicar()
  def multiplicar(self, valor1, valor2):
    total = valor1 * valor2
    return total
  
  # método dividir()
  def dividir(self, valor1, valor2):
    if valor2 == 0:
      return "não existe divisão por ZERO!"
    else:
      total = valor1 / valor2
      return total
  
  # método subtrair()
  def subtrair(self, valor1, valor2):
    total = valor1 - valor2
    return total
  
  # método potencia()
  def potencia(self, valor1, valor2):
    total = valor1 ** valor2
    return total
  
  # método raiz()
  def raiz(self, valor1):
    total = valor1 ** (1/2)
    return total


