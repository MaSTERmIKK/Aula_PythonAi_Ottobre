

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
    


scelta = int(input("inserisci il limite"))
scelta2 = int(input("inserisci il limite"))
scelta3 = int(input("inserisci il limite"))

lista = [*range(scelta,scelta2,scelta3)]
        
print(lista)




