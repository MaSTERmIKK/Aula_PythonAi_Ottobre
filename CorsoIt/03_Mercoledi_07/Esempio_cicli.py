"""
CICLI FOR E WHILE IN PYTHON
- for
- while
- range()
- cicli su liste
- cicli su stringhe
- enumerate()
- break
- continue
- cicli annidati
- for else
- while else
"""


# ==============================================================
# 1. FOR BASE
# ==============================================================

for numero in range(5):
    print(numero)

print()


# ==============================================================
# 2. RANGE CON INIZIO E FINE
# ==============================================================

for numero in range(1, 6):
    print(numero)

print()


# ==============================================================
# 3. RANGE CON STEP
# ==============================================================

for numero in range(0, 11, 2):
    print(numero)

print()


# ==============================================================
# 4. RANGE DECRESCENTE
# ==============================================================

for numero in range(10, 0, -1):
    print(numero)

print()


# ==============================================================
# 5. FOR SU UNA LISTA
# ==============================================================

nomi = ["Mario", "Anna", "Luca"]

for nome in nomi:
    print(nome)

print()


# ==============================================================
# 6. FOR SU UNA STRINGA
# ==============================================================

parola = "Python"

for lettera in parola:
    print(lettera)

print()


# ==============================================================
# 7. FOR CON INDICE
# ==============================================================

nomi = ["Mario", "Anna", "Luca"]

for i in range(len(nomi)):
    print(i, nomi[i])

print()


# ==============================================================
# 8. ENUMERATE
# ==============================================================

for indice, nome in enumerate(nomi):
    print(indice, nome)

print()


# ==============================================================
# 9. FOR SU DIZIONARIO
# ==============================================================

persona = {
    "nome": "Mario",
    "eta": 25,
    "citta": "Torino"
}

for chiave, valore in persona.items():
    print(chiave, "->", valore)

print()


# ==============================================================
# 10. BREAK
# Interrompe completamente il ciclo
# ==============================================================

for numero in range(1, 11):

    if numero == 5:
        break

    print(numero)

print()


# ==============================================================
# 11. CONTINUE
# Salta solamente l'iterazione corrente
# ==============================================================

for numero in range(1, 11):

    if numero == 5:
        continue

    print(numero)

print()


# ==============================================================
# 12. CICLO FOR CON CONDIZIONE
# ==============================================================

numeri = [10, 15, 20, 25, 30]

for numero in numeri:

    if numero >= 20:
        print(numero)

print()


# ==============================================================
# 13. SOMMA CON FOR
# ==============================================================

numeri = [10, 20, 30, 40]

totale = 0

for numero in numeri:
    totale += numero

print("Totale:", totale)

print()


# ==============================================================
# 14. CICLI FOR ANNIDATI
# ==============================================================

for riga in range(3):

    for colonna in range(3):
        print(riga, colonna)

print()


# ==============================================================
# 15. CICLO SU MATRICE
# ==============================================================

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for riga in matrice:

    for elemento in riga:
        print(elemento, end=" ")

    print()

print()


# ==============================================================
# 16. WHILE BASE
# ==============================================================

numero = 1

while numero <= 5:

    print(numero)

    numero += 1

print()


# ==============================================================
# 17. WHILE DECRESCENTE
# ==============================================================

numero = 5

while numero > 0:

    print(numero)

    numero -= 1

print()


# ==============================================================
# 18. WHILE CON BREAK
# ==============================================================

numero = 1

while True:

    print(numero)

    if numero == 5:
        break

    numero += 1

print()


# ==============================================================
# 19. WHILE CON CONTINUE
# ==============================================================

numero = 0

while numero < 10:

    numero += 1

    if numero == 5:
        continue

    print(numero)

print()


# ==============================================================
# 20. WHILE CON CONDIZIONE BOOLEANA
# ==============================================================

attivo = True
contatore = 0

while attivo:

    print("Iterazione:", contatore)

    contatore += 1

    if contatore == 5:
        attivo = False

print()


# ==============================================================
# 21. FOR ELSE
# ELSE VIENE ESEGUITO SE IL CICLO TERMINA SENZA BREAK
# ==============================================================

for numero in range(5):

    print(numero)

else:
    print("Ciclo terminato normalmente")

print()


# ==============================================================
# 22. FOR ELSE CON BREAK
# ==============================================================

for numero in range(10):

    if numero == 5:
        print("Numero trovato")
        break

else:
    print("Numero non trovato")

print()


# ==============================================================
# 23. WHILE ELSE
# ==============================================================

numero = 1

while numero <= 5:

    print(numero)

    numero += 1

else:
    print("While terminato")

print()


# ==============================================================
# 24. CERCARE UN ELEMENTO
# ==============================================================

nomi = ["Mario", "Anna", "Luca", "Marco"]

ricerca = "Luca"

for nome in nomi:

    if nome == ricerca:
        print("Utente trovato:", nome)
        break

else:
    print("Utente non trovato")

print()


# ==============================================================
# 25. CONTARE ELEMENTI CON UN CICLO
# ==============================================================

numeri = [10, 25, 8, 40, 12, 50]

contatore = 0

for numero in numeri:

    if numero >= 20:
        contatore += 1

print("Numeri maggiori o uguali a 20:", contatore)

print()


# ==============================================================
# 26. TABELLINE CON CICLI ANNIDATI
# ==============================================================

for numero in range(1, 4):

    print("Tabellina del", numero)

    for moltiplicatore in range(1, 11):

        risultato = numero * moltiplicatore

        print(numero, "x", moltiplicatore, "=", risultato)

    print()


# ==============================================================
# 27. INPUT CONTROLLATO CON WHILE
# ==============================================================

numero = 0

while numero <= 0:

    numero = int(input("Inserisci un numero positivo: "))

    if numero <= 0:
        print("Valore non valido")

print("Numero accettato:", numero)

print()


# ==============================================================
# 28. MENU CON WHILE
# ==============================================================

scelta = 0

while scelta != 3:

    print("1 - Saluta")
    print("2 - Informazioni")
    print("3 - Esci")

    scelta = int(input("Scelta: "))

    if scelta == 1:
        print("Ciao!")

    elif scelta == 2:
        print("Programma Python")

    elif scelta == 3:
        print("Uscita")

    else:
        print("Scelta non valida")

    print()
