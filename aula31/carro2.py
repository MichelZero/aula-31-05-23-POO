#
# autores: Michel
#
# data: 31/05/2023

# Criando uma classe Carro 2

# Exercício: Criando uma classe de Carro

# Crie uma classe chamada Carro que represente um carro simples.
# A classe deve ter os seguintes atributos:
# - marca: uma string que representa a marca do carro
# - modelo: uma string que representa o modelo do carro
# - ano: um inteiro que representa o ano de fabricação do carro
# - cor: uma string que representa a cor do carro
# - combustível: uma string que representa o tipo de combustível do carro

# Além disso, a classe deve ter os seguintes métodos:
# - info(): um método que imprime as informações do carro, mostrando a marca, modelo, ano e cor.
# - pintar(cor_nova): um método que recebe uma nova cor como parâmetro e atualiza a cor do carro.
# - ligar(): um método que imprime uma mensagem dizendo que o carro está ligado.
# - acelerar(): um método que imprime uma mensagem dizendo que o carro está acelerando.
# - frear(): um método que imprime uma mensagem dizendo que o carro está freando.


class Carro:
    def __init__(self, marca, modelo, ano, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = combustivel

    def info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Combustível: {self.combustivel}")

    def pintar(self, cor_nova):
        self.cor = cor_nova

    def ligar(self):
        print("O carro está sendo ligado.")
        
    def acelerar(self):
        print("O carro está acelerando.")
        
    def frear(self):
        print("O carro está freando.")
        

