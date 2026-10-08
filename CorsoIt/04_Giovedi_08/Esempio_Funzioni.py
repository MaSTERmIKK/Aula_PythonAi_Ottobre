#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FUNZIONI IN PYTHON

- def
- Chiamata di una funzione
- Parametri e argomenti
- return
- Parametri di default
- Parametri nominati
- *args e **kwargs
- Scope delle variabili
- Lambda
- Ricorsione
- Funzioni come parametri
"""


# ==============================================================
# 1. FUNZIONE BASE
# ==============================================================

def saluta():
    print("Ciao!")

saluta()

print()


# ==============================================================
# 2. FUNZIONE RICHIAMATA PIÙ VOLTE
# ==============================================================

def messaggio():
    print("Benvenuto nel corso Python")

messaggio()
messaggio()
messaggio()

print()


# ==============================================================
# 3. FUNZIONE CON UN PARAMETRO
# ==============================================================

def saluta_nome(nome):
    print("Ciao", nome)

saluta_nome("Mario")
saluta_nome("Anna")

print()


# ==============================================================
# 4. FUNZIONE CON PIÙ PARAMETRI
# ==============================================================

def presenta(nome, eta):
    print(f"Mi chiamo {nome} e ho {eta} anni")

presenta("Luca", 25)

print()


# ==============================================================
# 5. FUNZIONE CON RETURN
# Restituisce un valore al chiamante
# ==============================================================

def somma(a, b):
    risultato = a + b
    return risultato

totale = somma(10, 20)

print("Risultato:", totale)

print()


# ==============================================================
# 6. DIFFERENZA TRA PRINT E RETURN
# ==============================================================

def stampa_somma(a, b):
    print(a + b)

def restituisci_somma(a, b):
    return a + b

stampa_somma(5, 3)

risultato = restituisci_somma(5, 3)

print("Valore restituito:", risultato)

print()


# ==============================================================
# 7. RETURN CON CONDIZIONE
# ==============================================================

def pari_dispari(numero):

    if numero % 2 == 0:
        return "Pari"
    else:
        return "Dispari"

print(pari_dispari(10))
print(pari_dispari(7))

print()


# ==============================================================
# 8. RETURN INTERROMPE LA FUNZIONE
# ==============================================================

def controlla_eta(eta):

    if eta < 18:
        return "Accesso negato"

    return "Accesso consentito"

print(controlla_eta(15))
print(controlla_eta(25))

print()


# ==============================================================
# 9. PARAMETRI DI DEFAULT
# ==============================================================

def saluto(nome="Utente"):
    print("Benvenuto", nome)

saluto()
saluto("Marco")

print()


# ==============================================================
# 10. PIÙ PARAMETRI DI DEFAULT
# ==============================================================

def crea_persona(nome, eta=18, citta="Torino"):

    print("Nome:", nome)
    print("Età:", eta)
    print("Città:", citta)

crea_persona("Anna")
crea_persona("Luca", 25)
crea_persona("Mario", 30, "Milano")

print()


# ==============================================================
# 11. PARAMETRI NOMINATI
# ==============================================================

def dati_utente(nome, cognome, eta):
    print(nome, cognome, eta)

dati_utente(
    eta=25,
    nome="Mario",
    cognome="Rossi"
)

print()


# ==============================================================
# 12. RETURN MULTIPLO
# Restituisce una tupla di valori
# ==============================================================

def operazioni(a, b):

    somma = a + b
    differenza = a - b
    prodotto = a * b

    return somma, differenza, prodotto

s, d, p = operazioni(10, 5)

print("Somma:", s)
print("Differenza:", d)
print("Prodotto:", p)

print()


# ==============================================================
# 13. FUNZIONE CHE UTILIZZA UNA LISTA
# ==============================================================

def calcola_media(numeri):

    totale = 0

    for numero in numeri:
        totale += numero

    return totale / len(numeri)

voti = [20, 25, 30, 28]

print("Media:", calcola_media(voti))

print()


# ==============================================================
# 14. FUNZIONE CHE RESTITUISCE UNA LISTA
# ==============================================================

def genera_numeri(limite):

    numeri = []

    for i in range(1, limite + 1):
        numeri.append(i)

    return numeri

lista = genera_numeri(5)

print(lista)

print()


# ==============================================================
# 15. FUNZIONE CHE MODIFICA UNA LISTA
# ==============================================================

def aggiungi_elemento(lista, elemento):
    lista.append(elemento)

nomi = ["Mario", "Anna"]

aggiungi_elemento(nomi, "Luca")

print(nomi)

print()


# ==============================================================
# 16. FUNZIONE CHE RICHIAMA UN'ALTRA FUNZIONE
# ==============================================================

def quadrato(numero):
    return numero ** 2

def stampa_quadrato(numero):
    risultato = quadrato(numero)
    print("Quadrato:", risultato)

stampa_quadrato(5)

print()


# ==============================================================
# 17. *ARGS
# Accetta un numero variabile di argomenti posizionali
# ==============================================================

def somma_tutti(*numeri):

    totale = 0

    for numero in numeri:
        totale += numero

    return totale

print(somma_tutti(1, 2))
print(somma_tutti(1, 2, 3))
print(somma_tutti(1, 2, 3, 4, 5))

print()


# ==============================================================
# 18. **KWARGS
# Accetta argomenti nominati in un dizionario
# ==============================================================

def stampa_informazioni(**dati):

    for chiave, valore in dati.items():
        print(chiave, ":", valore)

stampa_informazioni(
    nome="Mario",
    eta=30,
    citta="Roma"
)

print()


# ==============================================================
# 19. *ARGS E **KWARGS INSIEME
# ==============================================================

def funzione_completa(*args, **kwargs):

    print("Argomenti posizionali:")

    for valore in args:
        print(valore)

    print("Argomenti nominati:")

    for chiave, valore in kwargs.items():
        print(chiave, valore)

funzione_completa(
    10, 20, 30,
    nome="Anna",
    eta=25
)

print()


# ==============================================================
# 20. VARIABILI LOCALI
# ==============================================================

def esempio_locale():

    numero = 10

    print("Dentro:", numero)

esempio_locale()

# La variabile numero definita nella funzione
# non è accessibile direttamente all'esterno.

print()


# ==============================================================
# 21. VARIABILI GLOBALI
# ==============================================================

contatore = 0

def incrementa():

    global contatore

    contatore += 1

incrementa()
incrementa()

print("Contatore:", contatore)

print()


# ==============================================================
# 22. FUNZIONE LAMBDA
# Funzione anonima composta da una singola espressione
# ==============================================================

quadrato = lambda x: x ** 2

print(quadrato(5))

somma = lambda a, b: a + b

print(somma(10, 20))

print()


# ==============================================================
# 23. LAMBDA CON CONDIZIONE
# ==============================================================

controlla = lambda numero: "Pari" if numero % 2 == 0 else "Dispari"

print(controlla(8))
print(controlla(5))

print()


# ==============================================================
# 24. FUNZIONE COME PARAMETRO
# ==============================================================

def applica_operazione(numero, funzione):
    return funzione(numero)

def doppio(x):
    return x * 2

def triplo(x):
    return x * 3

print(applica_operazione(10, doppio))
print(applica_operazione(10, triplo))

print()


# ==============================================================
# 25. FUNZIONE RICORSIVA
# Una funzione che richiama sé stessa
# ==============================================================

def conto_alla_rovescia(numero):

    if numero == 0:
        print("Fine")
        return

    print(numero)

    conto_alla_rovescia(numero - 1)

conto_alla_rovescia(5)

print()


# ==============================================================
# 26. RICORSIONE CON RETURN
# ==============================================================

def fattoriale(numero):

    if numero <= 1:
        return 1

    return numero * fattoriale(numero - 1)

print("Fattoriale:", fattoriale(5))

print()


# ==============================================================
# 27. FUNZIONE CON INPUT UTENTE
# ==============================================================

def chiedi_nome():

    nome = input("Inserisci il nome: ")

    return nome

nome_utente = chiedi_nome()

print("Benvenuto", nome_utente)

print()


# ==============================================================
# 28. FUNZIONE CON CICLO WHILE
# ==============================================================

def menu():

    while True:

        print("1 - Saluta")
        print("2 - Informazioni")
        print("3 - Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            print("Ciao!")

        elif scelta == "2":
            print("Corso Python")

        elif scelta == "3":
            print("Uscita")
            break

        else:
            print("Scelta non valida")

# Decommentare per avviare il menu
# menu()

print()


# ==============================================================
# 29. ESEMPIO PRATICO: CALCOLATRICE
# ==============================================================

def calcolatrice(a, b, operazione):

    if operazione == "+":
        return a + b

    elif operazione == "-":
        return a - b

    elif operazione == "*":
        return a * b

    elif operazione == "/":

        if b == 0:
            return "Errore: divisione per zero"

        return a / b

    else:
        return "Operazione non valida"


print(calcolatrice(10, 5, "+"))
print(calcolatrice(10, 5, "-"))
print(calcolatrice(10, 5, "*"))
print(calcolatrice(10, 5, "/"))

print()


# ==============================================================
# 30. ESEMPIO PRATICO: GESTIONE STUDENTI
# ==============================================================

studenti = {}

def aggiungi_studente(nome, voti):
    studenti[nome] = voti

def media_studente(nome):

    if nome not in studenti:
        return None

    voti = studenti[nome]

    if len(voti) == 0:
        return None

    return sum(voti) / len(voti)

def stampa_studenti():

    for nome, voti in studenti.items():

        print("Studente:", nome)
        print("Voti:", voti)
        print("Media:", media_studente(nome))
        print()


aggiungi_studente("Mario", [25, 28, 30])
aggiungi_studente("Anna", [30, 29, 28])
aggiungi_studente("Luca", [20, 22, 25])

stampa_studenti()
