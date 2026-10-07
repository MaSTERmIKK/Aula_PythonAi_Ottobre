# Es_1

ripeti = "si"

while ripeti == "si":

    numero = int(input("Inserisci un numero: "))

    for i in range(numero, -1, -1):
        print(i)

    ripeti = input("Vuoi ripetere? si/no: ")
    
# Es_2 

contatore_primi = 0

while contatore_primi < 5:

    numero = int(input("Inserisci un numero: "))

    primo = True

    if numero < 2:
        primo = False

    if numero >= 2:
        for i in range(2, numero):
            if numero % i == 0:
                primo = False

    if primo == True:
        print("Il numero è primo")
        contatore_primi = contatore_primi + 1
    else:
        print("Il numero non è primo")

print("Hai inserito 5 numeri primi")

