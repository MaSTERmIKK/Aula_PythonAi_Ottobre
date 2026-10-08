# -------------- variabili
x = 2

# -------------- collezioni
lista = []

# -------------- funzioni
def saluta(nome:str):
    
    print("ciao ", nome)
    
def somma(a =0,b =0):
    
    print(a+b)
    
def moltiplicazione(a,b):
    
    return a*b
    
# -------------- esecuzione
x = int(input("dammi numeri uno"))
x2 = int(input("dammi numeri due"))

saluta("matteo")
somma(x,x2)

y = moltiplicazione(10,5) # è uguale a a*b
lista[0] = moltiplicazione(100,5) # è uguale a a*b

# usiamo i return per riempire a e b di somma
somma(moltiplicazione(100,5), moltiplicazione(100,5))


