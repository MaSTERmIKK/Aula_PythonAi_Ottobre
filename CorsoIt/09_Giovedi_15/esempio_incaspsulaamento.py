class Padre:

    def __init__(self, nome):
        # Variabile protetta
        self._nome = nome

    def mostra_nome(self):
        print("Padre:", self._nome)


class Figlio(Padre):

    def __init__(self,nome):
        super().__init__(self,nome)

        # Prendo il valore protetto del padre
        # e lo salvo in una variabile privata del figlio
        self.__nome = self._nome
        self._nome = ""

    def mostra_nome_figlio(self):
        print("Figlio:", self.__nome)
        
