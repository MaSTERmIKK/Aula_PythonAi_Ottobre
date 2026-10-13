#---------------------------------------------__repr__
class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

    def __repr__(self):
        return f"Studente(nome={self.nome}, voto={self.voto})"

s = Studente("Mario", 28)
print(s)   # Studente(nome=Mario, voto=28)
repr(s)    # "Studente(nome=Mario, voto=28)"


#---------------------------------------------__eq__
class Prodotto:
 def __init__(self, nome, prezzo):
   self.nome = nome
   self.prezzo = prezzo

 def __eq__(self, altro):
   return self.nome == altro.nome and self.prezzo == altro.prezzo

p1 = Prodotto("Penna", 2)
p2 = Prodotto("Penna", 2)

print(p1 == p2)



#---------------------------------------------__getattribute__
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def __getattribute__(self, attributo):
        print(f"Sto accedendo all'attributo: {attributo}")
        return super().__getattribute__(attributo)

p = Persona("Mario", 30)

# accesso agli attributi
print(p.nome)
print(p.eta)
