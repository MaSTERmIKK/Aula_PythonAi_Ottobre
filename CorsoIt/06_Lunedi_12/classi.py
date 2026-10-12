class Persona:
    
    # Metodo costruttore
    def __init__(self, nome:str, eta:int):
        self.nome = nome
        self.eta = eta
    
    # Variabile di classe
    cittadinanza = " "
    
    # Metodo di classe
    def saluta(self):
        return("ciao mirko")


# Inizializzazione del'oggetto tramite costruttore 
Ogg_1 = Persona("Luca",31)
Ogg_2 = Persona("Martina",17)

Ogg_2.nome = "Martina"

print(Ogg_1.nome)
print(Ogg_2.nome)

print(Ogg_1.saluta())