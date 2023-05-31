#
# autores: Michel
#
# data: 31/05/2023

from calculadora import Calculadora as Calc
from aula31.carro import Carro
from pessoa import Pessoa as P



calc1 = Calc()
carro1 = Carro()
carro2 = Carro()
p1 = P()
p2 = P()

# usando os objetos 
soma = calc1.somar(2,3)
print(f"a soma foi de: {soma}")

print(carro1)
print(carro2)
print(p1.nome)
#p2
print(f"nome original p2: {p2.nome}")
p2.nome = 'joão'
print(f"nome atualizado p2: {p2.nome}")

