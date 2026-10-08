

# ESERCIZIO 1
def indovina_numero():

    numero_segreto = int(input("dammi un numero da indovinare"))
    tentativo = 0

    while tentativo != numero_segreto:

        tentativo = int(input("Indovina il numero da 1 a 100: "))

        if tentativo < numero_segreto:
            print("Il numero da indovinare è più alto")

        elif tentativo > numero_segreto:
            print("Il numero da indovinare è più basso")

        else:
            print("Hai indovinato!", numero_segreto)


# ESERCIZIO 2
def fibonacci(numero):

    a = 0
    b = 1

    while a <= numero:

        print(a)

        prossimo = a + b
        a = b
        b = prossimo


# PROGRAMMA PRINCIPALE

scelta = ""

while scelta != "fine":

    scelta = input("Scrivi es1, es2 oppure fine: ")

    if scelta == "es1":
        indovina_numero()

    elif scelta == "es2":
        numero = int(input("Inserisci il valore massimo N: "))
        fibonacci(numero)

    elif scelta == "fine":
        print("Programma terminato")

    else:
        print("Sei un pippo")
    
    
    