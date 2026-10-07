

controllore = True
 
while controllore:
    
    print("ciao")
    
    scelta = input("scrivi end per uscire")
    if scelta.lower() == "end":
        controllore = False
        

while True:
    
    print("ciao")
    
    scelta = input("scrivi end per uscire")
    if scelta.lower() == "end":
        break
    


scelta = float(input("inserisci il limite"))
scelta2 = float(input("inserisci il limite"))
scelta3 = float(input("inserisci il limite"))

lista = [*range(scelta,scelta2,scelta3)]
        
print(lista)




