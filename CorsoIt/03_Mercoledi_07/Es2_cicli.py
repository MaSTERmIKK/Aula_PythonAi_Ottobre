

scelta = ""

while scelta != "fine":

    scelta = input("Scegli esercizio: es1 - es2 - es3 - fine: ")

    # ESERCIZIO 1
    if scelta == "es1":

        somma = 0
        numero = int(input("Inserisci un numero: "))

        while numero != 0:
            somma = somma + numero
            numero = int(input("Inserisci un altro numero: "))

        print("La somma totale è:", somma)


    # ESERCIZIO 2
    if scelta == "es2":

        parola = input("Inserisci una parola: ")

        for lettera in parola:
            print(lettera)


    # ESERCIZIO 3
    if scelta == "es3":

        massimo = int(input("Inserisci il numero massimo: "))
        step = int(input("Inserisci lo step: "))
        start = int(input("Inserisci lo start: "))

        for x in range(start, massimo + 1, step):
            print(x)


    if scelta != "es1" and scelta != "es2" and scelta != "es3" and scelta != "fine":
        print("Sei un pippo")


print("Programma terminato")
