def conta_fino_a(numero_massimo):

    numero = 1

    while numero <= numero_massimo:
        yield numero
        numero = numero + 1


n = int(input("Fino a che numero vuoi contare? "))

for valore in conta_fino_a(n):
    
    print(valore)