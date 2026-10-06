#-------------------------------------------------- Es 2

x = int(input("Inserisci un numero"))

if x > 10:
    
    x = int(input("Inserisci un numero"))
    if x > 50: 
         
        x = int(input("Inserisci un numero"))
        if x > 100:  
            
            print("hai vinto")
            
  
#-------------------------------------------------- Es 2
            
lista = [1,2,3]

scelta = input("cosa vuoi fare?")

if scelta == "aggiungi" :
    scelta2 = input("scegli una parola")
    lista.append(scelta2)
    
    print(lista)
elif scelta == "rimuovi":
    print("scegli cosa rimuovere fra: ", lista)
    scelta2 = input("scegli una parola")
    lista.remove(scelta2)
    
    print(lista)  
elif scelta == "modifica":
    print("scegli quale posizione modificare da 0 con limite a", len(lista)-1 )
    scelta2 = int(input("scegli una posizione"))
    scelta3 = input("scegli una parola da aggiungere")
    lista[scelta2] = scelta3
    
    print(lista)   
else: 
    print("Scelta sbagliata")
