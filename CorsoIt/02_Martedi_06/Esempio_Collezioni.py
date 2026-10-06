#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LISTE IN PYTHON

- Creazione
- Accesso agli elementi
- Modifica
- append()
- insert()
- extend()
- remove()
- pop()
- del
- Cicli
- Slicing
- Ordinamento
- Liste annidate
- List comprehension
"""


# ==============================================================
# 1. CREAZIONE DI UNA LISTA
# ==============================================================

numeri = [10, 20, 30, 40, 50]

print(numeri)
print()


# ==============================================================
# 2. LISTE CON TIPI DIVERSI
# ==============================================================

dati = ["Mario", 25, True, 1.75]

print(dati)
print()


# ==============================================================
# 3. ACCESSO AGLI ELEMENTI
# ==============================================================

frutti = ["mela", "banana", "pera", "kiwi"]

print(frutti[0])
print(frutti[1])
print(frutti[3])

print()


# ==============================================================
# 4. INDICI NEGATIVI
# ==============================================================

print(frutti[-1])   # Ultimo elemento
print(frutti[-2])   # Penultimo elemento

print()


# ==============================================================
# 5. MODIFICA DI UN ELEMENTO
# ==============================================================

frutti[1] = "arancia"

print(frutti)
print()


# ==============================================================
# 6. APPEND()
# Aggiunge un elemento alla fine
# ==============================================================

frutti.append("fragola")

print(frutti)
print()


# ==============================================================
# 7. INSERT()
# Inserisce un elemento in una posizione specifica
# ==============================================================

frutti.insert(1, "limone")

print(frutti)
print()


# ==============================================================
# 8. EXTEND()
# Unisce più elementi alla lista
# ==============================================================

altri_frutti = ["pesca", "ananas"]

frutti.extend(altri_frutti)

print(frutti)
print()


# ==============================================================
# 9. REMOVE()
# Elimina un elemento cercandolo per valore
# ==============================================================

frutti.remove("pera")

print(frutti)
print()


# ==============================================================
# 10. POP()
# Elimina e restituisce un elemento
# ==============================================================

ultimo = frutti.pop()

print("Elemento eliminato:", ultimo)
print(frutti)

print()


# ==============================================================
# 11. POP CON INDICE
# ==============================================================

elemento = frutti.pop(0)

print("Elemento eliminato:", elemento)
print(frutti)

print()


# ==============================================================
# 12. DEL
# ==============================================================

numeri = [10, 20, 30, 40]

del numeri[1]

print(numeri)
print()


# ==============================================================
# 13. LEN()
# ==============================================================

nomi = ["Anna", "Luca", "Marco", "Sara"]

print("Numero elementi:", len(nomi))
print()


# ==============================================================
# 14. CICLO FOR SU LISTA
# ==============================================================

for nome in nomi:
    print(nome)

print()


# ==============================================================
# 15. CICLO CON RANGE E INDICI
# ==============================================================

for i in range(len(nomi)):
    print(i, nomi[i])

print()


# ==============================================================
# 16. ENUMERATE()
# Ottiene indice e valore contemporaneamente
# ==============================================================

for indice, nome in enumerate(nomi):
    print(indice, nome)

print()


# ==============================================================
# 17. RICERCA CON IN
# ==============================================================

if "Anna" in nomi:
    print("Anna è presente")

if "Giovanni" not in nomi:
    print("Giovanni non è presente")

print()


# ==============================================================
# 18. INDEX()
# Trova la posizione di un elemento
# ==============================================================

posizione = nomi.index("Marco")

print("Marco si trova nella posizione:", posizione)
print()


# ==============================================================
# 19. COUNT()
# Conta quante volte compare un valore
# ==============================================================

voti = [18, 25, 30, 25, 28, 25]

print("Il voto 25 compare:", voti.count(25), "volte")
print()


# ==============================================================
# 20. SLICING
# ==============================================================

numeri = [10, 20, 30, 40, 50, 60]

print(numeri[1:4])
print(numeri[:3])
print(numeri[3:])
print(numeri[::2])

print()


# ==============================================================
# 21. INVERTIRE UNA LISTA CON SLICING
# ==============================================================

print(numeri[::-1])
print()


# ==============================================================
# 22. SORT()
# Modifica direttamente la lista
# ==============================================================

numeri = [40, 10, 50, 20, 30]

numeri.sort()

print(numeri)

numeri.sort(reverse=True)

print(numeri)
print()


# ==============================================================
# 23. SORTED()
# Crea una nuova lista ordinata
# ==============================================================

numeri = [5, 2, 8, 1]

ordinati = sorted(numeri)

print("Originale:", numeri)
print("Ordinata:", ordinati)

print()


# ==============================================================
# 24. REVERSE()
# ==============================================================

numeri.reverse()

print(numeri)
print()


# ==============================================================
# 25. MIN, MAX E SUM
# ==============================================================

voti = [18, 25, 30, 27, 22]

print("Minimo:", min(voti))
print("Massimo:", max(voti))
print("Somma:", sum(voti))

print()


# ==============================================================
# 26. MEDIA DI UNA LISTA
# ==============================================================

media = sum(voti) / len(voti)

print("Media:", media)
print()


# ==============================================================
# 27. LISTE ANNIDATE
# ==============================================================

studenti = [
    ["Mario", 25],
    ["Anna", 30],
    ["Luca", 28]
]

print(studenti)
print(studenti[0])
print(studenti[0][0])
print(studenti[0][1])

print()


# ==============================================================
# 28. CICLO SU LISTE ANNIDATE
# ==============================================================

for studente in studenti:

    nome = studente[0]
    voto = studente[1]

    print("Nome:", nome)
    print("Voto:", voto)

print()


# ==============================================================
# 29. UNPACKING NEL CICLO
# ==============================================================

for nome, voto in studenti:
    print(nome, "->", voto)

print()


# ==============================================================
# 30. MATRICE CON LISTE
# ==============================================================

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrice)

print("Elemento:", matrice[1][2])

print()


# ==============================================================
# 31. CICLO SU MATRICE
# ==============================================================

for riga in matrice:

    for numero in riga:
        print(numero, end=" ")

    print()

print()


# ==============================================================
# 32. LIST COMPREHENSION
# ==============================================================

quadrati = [x ** 2 for x in range(1, 6)]

print(quadrati)
print()


# ==============================================================
# 33. LIST COMPREHENSION CON CONDIZIONE
# ==============================================================

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pari = [x for x in numeri if x % 2 == 0]

print(pari)
print()


# ==============================================================
# 34. COPIA DI UNA LISTA
# ==============================================================

lista1 = [1, 2, 3]

lista2 = lista1.copy()

lista2.append(4)

print("Lista 1:", lista1)
print("Lista 2:", lista2)

print()


# ==============================================================
# 35. ATTENZIONE ALL'ASSEGNAZIONE
# ==============================================================

lista1 = [1, 2, 3]

lista2 = lista1

lista2.append(4)

# Entrambe cambiano perché fanno riferimento
# alla stessa lista

print("Lista 1:", lista1)
print("Lista 2:", lista2)

print()


# ==============================================================
# 36. CLEAR()
# ==============================================================

numeri = [1, 2, 3, 4]

numeri.clear()

print(numeri)
print()


# ==============================================================
# 37. ESEMPIO PRATICO: LISTA VOTI
# ==============================================================

voti = [25, 18, 30, 27, 22, 30]

totale = 0

for voto in voti:
    totale += voto

media = totale / len(voti)

print("Voti:", voti)
print("Numero voti:", len(voti))
print("Media:", round(media, 2))
print("Voto massimo:", max(voti))
print("Voto minimo:", min(voti))

print()


# ==============================================================
# 38. FILTRARE UNA LISTA
# ==============================================================

voti_sufficienti = []

for voto in voti:

    if voto >= 18:
        voti_sufficienti.append(voto)

print("Voti sufficienti:", voti_sufficienti)
