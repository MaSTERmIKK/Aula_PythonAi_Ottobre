from abc import ABC, abstractmethod


class Pippo_Astratto(ABC):
    
    x = 10
    
    def ciao(self):
        print("ciao")
        
    @abstractmethod
    def Metodo_obbligatorio(self):
        pass
    
    @abstractmethod
    def Metodo_obbligatorio2(self):
        pass
    
    
    
class Pippo_reale(Pippo_Astratto):
    
    def Metodo_obbligatorio(self):
        print("sono reale")
        
    def Metodo_obbligatorio2(self):
        print("sono reale 2")

        
        
P_r = Pippo_reale()  # dai figli si

# P_a = Pippo_Astratto()  Non si può creare un oggeto tramite una classe astratta