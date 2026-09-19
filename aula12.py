# comentario
""" comentario """
class Biscoito():
    #Método construtor que instancia o objeto
    tamanho = "4 cm"
    peso = "0,2 kg"
    temperatura = "35 graus"

    def __init__(self, tamanho, peso, temperatura):
        self.tamanho = tamanho
        self.peso = peso
        self.temperatura = temperatura

    #Método de classe
    def informacoes(self):
        return "informações: ", self.tamanho, self.peso, self.temperatura

    #Getters
    def get_tamanho(self):
        return self.tamanho

    #Setters
    def set_tamanho(self, tamanhoNovo):
        self.tamanho = tamanhoNovo
        
#Acessando atributo de um objeto
biscoito = Biscoito(tamanho ="4 cm", peso="0,2 kg", temperatura="35 graus")

#Acessando método de um objeto
print (biscoito.tamanho)
print (biscoito.informacoes())

biscoito2 = Biscoito(tamanho ="8 cm", peso="1 kg", temperatura="40 graus")
print (biscoito2.tamanho)
print (biscoito2.informacoes())
