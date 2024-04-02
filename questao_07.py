#ANCHOR - O que é uma classe?
#Descreve atributos e métodos que os obejtos criados terão

#ANCHOR - Quais as vantagens de utilizar uma classe?
#Organização e abstrair maior detalhes do bbjeto

#ANCHOR - Em um programa funcional a classe é importante?
#

#ANCHOR - O que vem a ser paradigma de programação?
#

#ANCHOR - O pyhton é multi paradigma? Explique?
# 
class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def get_nome(self):
        return self.nome

    def get_marca(self):
        return self.marca

carro = Carro(nome="Fusca", marca="Volkswagen")
print(f"Nome do carro: {carro.get_nome()}")
print(f"Marca do carro: {carro.get_marca()}")
