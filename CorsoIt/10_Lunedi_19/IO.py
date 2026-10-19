def modalita_lettura():
    # Valorizzazione pseudo oggetto dal file
    File_valorrizato_da_open = open("CorsoIt/10_Lunedi_19/pippo.txt","r")

    # metodo di lettura totale del file
    contenuto_file_totale = File_valorrizato_da_open.read()
    print(contenuto_file_totale)

    # metodo di lettura line by line del file
    contenuto_file_riga = File_valorrizato_da_open.readline()
    print(contenuto_file_riga)

    File_valorrizato_da_open.close()

File_valorrizato_da_open = open("CorsoIt/10_Lunedi_19/pippo.txt","w")

with open("CorsoIt/10_Lunedi_19/pippo.txt","r"):
    pass