#---------------------------------------ES1

class punto:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "ciao sono un str"
        
    def muovi_punti(self, dx, dy):
        self.x= dx
        self.y= dy
        
    def distanza_ordigine(self):
        return self.x, self.y


'''x = input()
y = input()

punto_mio = punto(x,y)
print(punto_mio)'''


#---------------------------------------ES2

class libro:
    
    def __init__(self, pagine, autore, titolo):
        self.pagine = pagine
        self.autore = autore
        self.titolo = titolo
        
    def stampa_libro(self):
        return self.autore, self.pagine, self.titolo

scelta = ""
lista_libri = []
while scelta != "end" :
    
    in1 = input("pagine?")
    in2 = input("autore?")
    in3 = input("titolo?")
    
    Obj = libro(in1,in2,in3)
    print(Obj.stampa_libro())
    lista_libri.append(Obj)
    
   
    scelta= input("vuoi continuare?")
    
for i in lista_libri:
    
    print(i.stampa_libro())
    

#----------------------------------------Es3

class ContoBncario:
    
    def __init__(self, intestatario, saldo):
        self.intestatario = intestatario
        self.saldo = saldo
        
    def deposita(self):
        pass

    def ritira(self):
        pass
    
    def viss(self):
        pass
 
 
 
scelta_menu = ""
while scelta_menu != "end" :
   pass


