
x = 30
x = "pippo"


class Pippo():
    def fai_cosa_a_caso(self):
        print("cosa a caso pippo")

        
class Pappo():
    def fai_cosa_a_caso(self):
        print("cosa a caso pappo")
        

pippo = Pippo()
pappo = Pappo()

def fai_cose(oggetto_a_caso:object):
    
    oggetto_a_caso.fai_cosa_a_caso()
    
fai_cose(pappo)




