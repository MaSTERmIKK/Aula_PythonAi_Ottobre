
# Funzione per creare un file
def crea_file(nome):
    file = open(nome, "w")
    file.close()
    print("File creato correttamente!")


# Funzione per modificare un file
def modifica_file(nome):
    testo = input("Inserisci il testo da aggiungere: ")

    file = open(nome, "a")
    file.write(testo + "\n")
    file.close()

    print("File modificato correttamente!")


# Funzione per leggere un file
def leggi_file(nome):
    file = open(nome, "r")
    contenuto = file.read()
    file.close()

    print("Contenuto del file:")
    print(contenuto)


# Funzione per svuotare un file
def svuota_file(nome):
    file = open(nome, "w")
    file.close()

    print("File svuotato correttamente!")


# Programma principale
while True:

    print("\n--- MENU FILE ---")
    print("1. Crea file")
    print("2. Modifica file")
    print("3. Leggi file")
    print("4. Svuota file")
    print("5. Esci")

    scelta = input("Scegli un'operazione: ")

    if scelta == "5":
        print("Programma terminato!")
        break

    if scelta == "1" or scelta == "2" or scelta == "3" or scelta == "4":

        nome = input("Inserisci il nome del file: ")
        nome = nome + ".txt"

        try:
            if scelta == "1":
                crea_file(nome)

            elif scelta == "2":
                modifica_file(nome)

            elif scelta == "3":
                leggi_file(nome)

            elif scelta == "4":
                svuota_file(nome)

        except FileNotFoundError:
            print("Errore: il file non esiste!")

    else:
        print("Scelta non valida!")
