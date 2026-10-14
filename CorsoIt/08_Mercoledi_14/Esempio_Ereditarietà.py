#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EREDITARIETÀ IN PYTHON

- Ereditarietà semplice
- Classe padre e classe figlia
- Ereditarietà dei metodi
- Ereditarietà degli attributi
- __init__ nelle sottoclassi
- super()
- Override dei metodi
- Estensione dei metodi
- Ereditarietà multilivello
- Ereditarietà gerarchica
- Ereditarietà multipla
- isinstance()
- issubclass()
- Method Resolution Order (MRO)
- Polimorfismo tramite ereditarietà
"""


# ==============================================================
# 1. EREDITARIETÀ SEMPLICE
# ==============================================================

class Animale:

    def mangia(self):
        print("L'animale sta mangiando")


class Cane(Animale):
    pass


cane = Cane()

# Il metodo appartiene alla classe padre
cane.mangia()

print()


# ==============================================================
# 2. CLASSE PADRE E CLASSE FIGLIA
# ==============================================================

class Persona:

    def saluta(self):
        print("Ciao, sono una persona")


class Studente(Persona):

    def studia(self):
        print("Sto studiando Python")


studente = Studente()

# Metodo ereditato
studente.saluta()

# Metodo della classe figlia
studente.studia()

print()


# ==============================================================
# 3. EREDITARIETÀ DEGLI ATTRIBUTI
# ==============================================================

class Veicolo:

    ruote = 4

    def descrizione(self):
        print("Sono un veicolo")


class Automobile(Veicolo):

    marca = "Fiat"


auto = Automobile()

print("Marca:", auto.marca)
print("Ruote:", auto.ruote)

auto.descrizione()

print()


# ==============================================================
# 4. COSTRUTTORE EREDITATO
# ==============================================================

class Utente:

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta


class Cliente(Utente):
    pass


cliente = Cliente("Mario", 30)

print(cliente.nome)
print(cliente.eta)

print()


# ==============================================================
# 5. SUPER()
# Richiama il costruttore della classe padre
# ==============================================================

class Dipendente:

    def __init__(self, nome, stipendio):
        self.nome = nome
        self.stipendio = stipendio


class Programmatore(Dipendente):

    def __init__(self, nome, stipendio, linguaggio):

        super().__init__(nome, stipendio)

        self.linguaggio = linguaggio


programmatore = Programmatore(
    "Anna",
    2500,
    "Python"
)

print(programmatore.nome)
print(programmatore.stipendio)
print(programmatore.linguaggio)

print()


# ==============================================================
# 6. OVERRIDE DEI METODI
# La classe figlia ridefinisce un metodo del padre
# ==============================================================

class Animale:

    def verso(self):
        print("Verso generico")


class Cane(Animale):

    def verso(self):
        print("Bau")


class Gatto(Animale):

    def verso(self):
        print("Miao")


cane = Cane()
gatto = Gatto()

cane.verso()
gatto.verso()

print()


# ==============================================================
# 7. SUPER() NEI METODI
# Esegue anche il comportamento del padre
# ==============================================================

class Persona:

    def presentati(self):
        print("Sono una persona")


class Professore(Persona):

    def presentati(self):

        super().presentati()

        print("Insegno programmazione")


professore = Professore()

professore.presentati()

print()


# ==============================================================
# 8. ESTENSIONE DI UN METODO EREDITATO
# ==============================================================

class Conto:

    def __init__(self, saldo):
        self.saldo = saldo

    def deposita(self, importo):

        if importo > 0:
            self.saldo += importo


class ContoPremium(Conto):

    def deposita(self, importo):

        # Esegue prima il metodo del padre
        super().deposita(importo)

        # Aggiunge un comportamento
        if importo > 100:
            self.saldo += 5


conto = ContoPremium(100)

conto.deposita(200)

print("Saldo:", conto.saldo)

print()


# ==============================================================
# 9. EREDITARIETÀ MULTILIVELLO
# Una classe eredita da una classe già derivata
# ==============================================================

class EssereVivente:

    def vivere(self):
        print("Sono un essere vivente")


class Animale(EssereVivente):

    def muoversi(self):
        print("Mi sto muovendo")


class Cane(Animale):

    def abbaiare(self):
        print("Bau!")


cane = Cane()

cane.vivere()
cane.muoversi()
cane.abbaiare()

print()


# ==============================================================
# 10. EREDITARIETÀ GERARCHICA
# Più classi ereditano dalla stessa classe padre
# ==============================================================

class Veicolo:

    def accendi(self):
        print("Motore acceso")


class Auto(Veicolo):

    def guida(self):
        print("Sto guidando")


class Moto(Veicolo):

    def impenna(self):
        print("Sto impennando")


auto = Auto()
moto = Moto()

auto.accendi()
auto.guida()

moto.accendi()
moto.impenna()

print()


# ==============================================================
# 11. EREDITARIETÀ MULTIPLA
# Una classe eredita da più classi
# ==============================================================

class Nuotatore:

    def nuota(self):
        print("Sto nuotando")


class Corridore:

    def corri(self):
        print("Sto correndo")


class Atleta(Nuotatore, Corridore):
    pass


atleta = Atleta()

atleta.nuota()
atleta.corri()

print()


# ==============================================================
# 12. EREDITARIETÀ MULTIPLA CON METODI UGUALI
# ==============================================================

class ClasseA:

    def saluta(self):
        print("Saluto dalla classe A")


class ClasseB:

    def saluta(self):
        print("Saluto dalla classe B")


class ClasseC(ClasseA, ClasseB):
    pass


oggetto = ClasseC()

# Python cerca il metodo secondo la MRO
oggetto.saluta()

print()


# ==============================================================
# 13. METHOD RESOLUTION ORDER (MRO)
# Ordine di ricerca dei metodi
# ==============================================================

print("MRO:", ClasseC.mro())

for classe in ClasseC.__mro__:
    print(classe.__name__)

print()


# ==============================================================
# 14. ISSUBCLASS()
# Controlla se una classe deriva da un'altra
# ==============================================================

class Animale:
    pass


class Cane(Animale):
    pass


class Gatto(Animale):
    pass


print(issubclass(Cane, Animale))
print(issubclass(Gatto, Animale))
print(issubclass(Cane, Gatto))

print()


# ==============================================================
# 15. ISINSTANCE()
# Controlla se un oggetto è istanza di una classe
# o di una sua sottoclasse
# ==============================================================

cane = Cane()

print(isinstance(cane, Cane))
print(isinstance(cane, Animale))
print(isinstance(cane, Gatto))

print()


# ==============================================================
# 16. TYPE() E ISINSTANCE()
# ==============================================================

class Persona:
    pass


class Studente(Persona):
    pass


studente = Studente()

print(type(studente) == Studente)

# False: il tipo esatto non è Persona
print(type(studente) == Persona)

# True: Studente eredita da Persona
print(isinstance(studente, Persona))

print()


# ==============================================================
# 17. POLIMORFISMO TRAMITE EREDITARIETÀ
# ==============================================================

class Animale:

    def verso(self):
        print("Verso generico")


class Cane(Animale):

    def verso(self):
        print("Bau")


class Gatto(Animale):

    def verso(self):
        print("Miao")


class Mucca(Animale):

    def verso(self):
        print("Muu")


animali = [
    Cane(),
    Gatto(),
    Mucca()
]

for animale in animali:
    animale.verso()

print()


# ==============================================================
# 18. FUNZIONE CHE ACCETTA OGGETTI DERIVATI
# ==============================================================

def fai_parlare(animale):
    animale.verso()


fai_parlare(Cane())
fai_parlare(Gatto())
fai_parlare(Mucca())

print()


# ==============================================================
# 19. OVERRIDE DI UN METODO SPECIALE
# ==============================================================

class Persona:

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Persona: {self.nome}"


class Studente(Persona):

    def __init__(self, nome, voto):

        super().__init__(nome)

        self.voto = voto

    def __str__(self):
        return f"{super().__str__()}, voto: {self.voto}"


studente = Studente("Mario", 28)

print(studente)

print()


# ==============================================================
# 20. EREDITARIETÀ CON ATTRIBUTI DI CLASSE
# ==============================================================

class Dipendente:

    azienda = "Python SRL"


class Manager(Dipendente):
    pass


manager = Manager()

print(manager.azienda)

# Modifica solo l'attributo della sottoclasse
Manager.azienda = "Python Academy"

print("Manager:", Manager.azienda)
print("Dipendente:", Dipendente.azienda)

print()


# ==============================================================
# 21. ESEMPIO COMPLETO: PERSONAGGI DI UN VIDEOGIOCO
# ==============================================================

class Personaggio:

    def __init__(self, nome, vita, attacco):

        self.nome = nome
        self.vita = vita
        self.attacco = attacco

    def attacca(self, bersaglio):

        bersaglio.vita = max(
            0,
            bersaglio.vita - self.attacco
        )

        print(
            self.nome,
            "attacca",
            bersaglio.nome
        )

    def mostra_stato(self):

        print(
            f"{self.nome} - Vita: {self.vita}"
        )


class Guerriero(Personaggio):

    def __init__(self, nome):

        super().__init__(
            nome,
            vita=150,
            attacco=25
        )

    def attacca(self, bersaglio):

        print("Attacco con spada!")

        super().attacca(bersaglio)


class Mago(Personaggio):

    def __init__(self, nome):

        super().__init__(
            nome,
            vita=80,
            attacco=40
        )

    def attacca(self, bersaglio):

        print("Lancio una magia!")

        super().attacca(bersaglio)


class Arciere(Personaggio):

    def __init__(self, nome):

        super().__init__(
            nome,
            vita=100,
            attacco=30
        )

    def attacca(self, bersaglio):

        print("Scocco una freccia!")

        super().attacca(bersaglio)


guerriero = Guerriero("Arthur")
mago = Mago("Merlin")
arciere = Arciere("Robin")

personaggi = [
    guerriero,
    mago,
    arciere
]

# Tutti condividono la stessa interfaccia
for personaggio in personaggi:
    personaggio.mostra_stato()

print()

# I metodi vengono eseguiti secondo la classe
guerriero.attacca(mago)
mago.attacca(guerriero)
arciere.attacca(mago)

print()

for personaggio in personaggi:
    personaggio.mostra_stato()