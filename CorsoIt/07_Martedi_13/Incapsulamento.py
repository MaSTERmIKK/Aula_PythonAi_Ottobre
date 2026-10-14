
#lvl_0
class x:
    #lvl_1
    def y():
        #lvl_2
        if True:
            #lvl_3
            pass
        
class Parametri_privati():
    # variabile privata
    __nome = "mirko"
    # variabile protetta
    _protetto = ""
    
    def __init__(self, nome):
        self.__nome = nome     
    # getter e setter
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome_nuovo):
        if len(nome_nuovo) < 0 :
            print("sei un pippo")
        else:
            self.__nome = nome_nuovo
    # metodo privato
    def __metodo_privato(self):
        print("sono dentro")
    
O_pp = Parametri_privati("mirko")
print(O_pp.get_nome())
O_pp.set_nome("Marco")
print(O_pp.get_nome())

print(O_pp._protetto)
