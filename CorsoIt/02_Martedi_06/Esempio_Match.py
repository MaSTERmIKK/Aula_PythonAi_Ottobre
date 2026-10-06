#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MATCH - CASE IN PYTHON

Disponibile da Python 3.10.

- match base
- case
- case _
- più valori
- match con numeri
- match con stringhe
- operatore |
- guard con if
- tuple
- liste
- dizionari
- esempio menu
"""


# ==============================================================
# 1. MATCH BASE
# ==============================================================

giorno = 1

match giorno:

    case 1:
        print("Lunedì")

    case 2:
        print("Martedì")

    case 3:
        print("Mercoledì")


print()


# ==============================================================
# 2. CASE DI DEFAULT
# case _ equivale concettualmente al default
# ==============================================================

giorno = 8

match giorno:

    case 1:
        print("Lunedì")

    case 2:
        print("Martedì")

    case 3:
        print("Mercoledì")

    case _:
        print("Giorno non valido")


print()


# ==============================================================
# 3. MATCH CON STRINGHE
# ==============================================================

comando = "start"

match comando:

    case "start":
        print("Avvio programma")

    case "stop":
        print("Arresto programma")

    case "pause":
        print("Programma in pausa")

    case _:
        print("Comando sconosciuto")


print()


# ==============================================================
# 4. PIÙ VALORI NELLO STESSO CASE
# ==============================================================

giorno = "sabato"

match giorno:

    case "sabato" | "domenica":
        print("Weekend")

    case "lunedì" | "martedì" | "mercoledì" | "giovedì" | "venerdì":
        print("Giorno lavorativo")

    case _:
        print("Giorno non valido")


print()


# ==============================================================
# 5. MATCH CON NUMERI
# ==============================================================

scelta = 2

match scelta:

    case 1:
        print("Nuova partita")

    case 2:
        print("Carica partita")

    case 3:
        print("Impostazioni")

    case 4:
        print("Esci")

    case _:
        print("Scelta non valida")


print()


# ==============================================================
# 6. MATCH CON GUARD
# Aggiungiamo una condizione IF al CASE
# ==============================================================

numero = 20

match numero:

    case n if n > 0:
        print("Numero positivo")

    case n if n < 0:
        print("Numero negativo")

    case 0:
        print("Zero")


print()


# ==============================================================
# 7. MATCH CON INTERVALLI
# ==============================================================

voto = 27

match voto:

    case voto if voto < 0 or voto > 30:
        print("Voto non valido")

    case voto if voto >= 28:
        print("Ottimo")

    case voto if voto >= 24:
        print("Buono")

    case voto if voto >= 18:
        print("Sufficiente")

    case _:
        print("Insufficiente")


print()


# ==============================================================
# 8. MATCH CON TUPLE
# ==============================================================

punto = (0, 5)

match punto:

    case (0, 0):
        print("Origine")

    case (0, y):
        print("Asse Y:", y)

    case (x, 0):
        print("Asse X:", x)

    case (x, y):
        print("Coordinate:", x, y)


print()


# ==============================================================
# 9. MATCH CON LISTE
# ==============================================================

dati = ["Mario", 25]

match dati:

    case [nome, eta]:
        print("Nome:", nome)
        print("Età:", eta)

    case _:
        print("Formato non valido")


print()


# ==============================================================
# 10. MATCH CON LISTE DI LUNGHEZZA DIFFERENTE
# ==============================================================

dati = ["Anna", 30, "Torino"]

match dati:

    case [nome]:
        print("Solo nome:", nome)

    case [nome, eta]:
        print(nome, eta)

    case [nome, eta, citta]:
        print(nome, eta, citta)

    case _:
        print("Struttura sconosciuta")


print()


# ==============================================================
# 11. CATTURARE PIÙ ELEMENTI CON *
# ==============================================================

numeri = [10, 20, 30, 40, 50]

match numeri:

    case [primo, secondo, *resto]:

        print("Primo:", primo)
        print("Secondo:", secondo)
        print("Resto:", resto)


print()


# ==============================================================
# 12. MATCH CON DIZIONARI
# ==============================================================

utente = {
    "nome": "Mario",
    "ruolo": "admin"
}

match utente:

    case {"nome": nome, "ruolo": "admin"}:
        print(nome, "è amministratore")

    case {"nome": nome, "ruolo": "utente"}:
        print(nome, "è utente")

    case _:
        print("Utente sconosciuto")


print()


# ==============================================================
# 13. MATCH CON DIZIONARIO + GUARD
# ==============================================================

prodotto = {
    "nome": "PC",
    "prezzo": 1500
}

match prodotto:

    case {"nome": nome, "prezzo": prezzo} if prezzo >= 1000:
        print(nome, "è un prodotto costoso")

    case {"nome": nome, "prezzo": prezzo}:
        print(nome, "costa", prezzo)

    case _:
        print("Prodotto non valido")


print()


# ==============================================================
# 14. MATCH CON TIPO DI STRUTTURA
# ==============================================================

dato = [10, 20]

match dato:

    case [x, y]:
        print("Lista con due elementi:", x, y)

    case {"nome": nome}:
        print("Dizionario con nome:", nome)

    case _:
        print("Altra struttura")


print()


# ==============================================================
# 15. MATCH DENTRO UNA FUNZIONE
# ==============================================================

def operazione(scelta, a, b):

    match scelta:

        case "somma":
            return a + b

        case "sottrazione":
            return a - b

        case "moltiplicazione":
            return a * b

        case "divisione":

            if b != 0:
                return a / b

            return "Divisione per zero"

        case _:
            return "Operazione sconosciuta"


print(operazione("somma", 10, 5))
print(operazione("moltiplicazione", 10, 5))

print()


# ==============================================================
# 16. ESEMPIO PRATICO: MENU
# ==============================================================

scelta = int(input(
    "1 - Nuova partita\n"
    "2 - Carica partita\n"
    "3 - Impostazioni\n"
    "4 - Esci\n"
    "Scelta: "
))

match scelta:

    case 1:
        print("Nuova partita avviata")

    case 2:
        print("Caricamento partita")

    case 3:
        print("Apertura impostazioni")

    case 4:
        print("Uscita dal programma")

    case _:
        print("Scelta non valida")
