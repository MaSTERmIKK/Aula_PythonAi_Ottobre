lista_n = [1,2,3,4]
lista_s = ["m", "n", "o"]

choose = input("Inserisci al tua choose tra: S e N")

if choose.upper == "S":
    
    choose = input("Inserisci al tua choose tra: AGGIUNGERE e RIMUOVERE")

    if choose.upper == "AGGIUNGERE":
        choose = input("Inserisci LA PAROLA DA AGGIUNGERE")
        lista_s.append(choose)
        print(lista_s)
    elif choose.upper == "RIMUOVERE":
        choose = input("Inserisci LA PAROLA DA rimuovere tra: ", lista_s)
        lista_s.remove(choose)
        print(lista_s)  
    
elif choose.upper == "N":
    
    choose = input("Inserisci al tua choose tra: AGGIUNGERE e RIMUOVERE")

    if choose.upper == "AGGIUNGERE":
        choose = int(input("Inserisci LA numero DA AGGIUNGERE"))
        lista_s.append(choose)
        print(lista_s)
        
    elif choose.upper == "RIMUOVERE":
        choose = int(input("Inserisci il numero DA rimuovere tra: ", lista_n))
        lista_n.remove(choose)
        print(lista_s)  
    
else:
    print("sei un pippo")