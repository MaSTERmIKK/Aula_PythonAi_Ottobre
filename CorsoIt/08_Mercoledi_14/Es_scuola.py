# =========================
# CLASSE BASE: PERSONA
# =========================

class Persona:

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def presentazione(self):
        print("Nome:", self.nome)
        print("Età:", self.eta)


# =========================
# CLASSE STUDENTE
# =========================

class Studente(Persona):

    def __init__(self, nome, eta, voti:list):
        # Richiamo il costruttore della classe Persona
        super().__init__(nome, eta)
        self.voti = voti

    def calcola_media(self):

        if len(self.voti) == 0:
            return 0

        somma = 0

        for voto in self.voti:
            somma = somma + voto

        return somma / len(self.voti)

    def presentazione(self):

        # Override del metodo della classe Persona
        print("Studente:", self.nome)
        print("Età:", self.eta)
        print("Media:", self.calcola_media())


# =========================
# CLASSE PROFESSORE
# =========================

class Professore(Persona):

    def __init__(self, nome, eta, materia):

        # Richiamo il costruttore della classe Persona
        super().__init__(nome, eta)

        self.__materia = materia

    def presentazione(self):

        # Override del metodo della classe Persona
        print("Professore:", self.nome)
        print("Età:", self.eta)
        print("Materia:", self.get_materia())
        
    def get_materia(self):
        return self.__materia

    def set_materia(self, nuova_materia):
        self.__materia= nuova_materia
        return "Materia cambiata"


# =========================
# CLASSE SCUOLA
# =========================

class Scuola:

    def __init__(self):

        # Liste che conterranno gli oggetti creati
        self.studenti = []
        self.professori = []

    def inserisci_studente(self):

        nome = input("Nome studente: ")
        eta = int(input("Età studente: "))

        voti = []

        quanti_voti = int(input("Quanti voti vuoi inserire? "))

        for i in range(quanti_voti):

            voto = int(input("Inserisci voto: "))
            voti.append(voto)

        # Creo l'oggetto Studente
        studente = Studente(nome, eta, voti)

        # Lo salvo nella scuola
        self.studenti.append(studente)

        print("Studente inserito correttamente")


    def inserisci_professore(self):

        nome = input("Nome professore: ")
        eta = int(input("Età professore: "))
        materia = input("Materia insegnata: ")

        # Creo l'oggetto Professore
        professore = Professore(nome, eta, materia)

        # Lo salvo nella scuola
        self.professori.append(professore)

        print("Professore inserito correttamente")


    def mostra_persone(self):
        
        scelta = int(input("vuoi gli studenti 1 o i prof 2"))

        if scelta == 1:
            print("\n--- STUDENTI ---")

            for studente in self.studenti:
                studente.presentazione()
                print()
                
        if scelta == 2:            
            print("\n--- PROFESSORI ---")
            
            for professore in self.professori:
                professore.presentazione()
                print()
    
    def compresione_oggetto(self):
        
        if isinstance(self, Studente):
            print(self.nome, "è uno studente")
        elif isinstance(self, Professore):
            print(self.nome, "è un professore")
            

# =========================
# PROGRAMMA PRINCIPALE
# =========================

scuola = Scuola()

scelta = ""

while scelta != "fine":

    print("\n--- GESTIONE SCUOLA ---")
    print("1 - Inserisci studente")
    print("2 - Inserisci professore")
    print("3 - Mostra studenti")
    print("4 - Mostra professori")
    print("fine - Esci")

    scelta = input("Scegli operazione: ")


    if scelta == "1":
        scuola.inserisci_studente()

    elif scelta == "2":
        scuola.inserisci_professore()

    elif scelta == "3":
        scuola.mostra_studenti()

    elif scelta == "4":
        scuola.mostra_professori()

    elif scelta == "fine":
        print("Programma terminato")

    else:
        print("Scelta non valida")