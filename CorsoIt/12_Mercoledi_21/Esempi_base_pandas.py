import pandas as pd

# Creazione di un DataFrame con dati di esempio
data = {
    'Nome': ['Alice', 'Bob', 'Carla'],
    'Età': [25, 30, 22],
    'Città': ['Roma', 'Milano', 'Napoli']
}

# aggiunta di una chiave al dizionario
data["Sesso"] = ["F","M","F"]
data["Exp"] = [120,35,105]

df = pd.DataFrame(data)

# Stampa del DataFrame originale
print("")
print("DataFrame Originale:")
print(df)
print("")

# head stampa le prime x righe e taiol stampa le ultime x righe 
# questa è l'esplorazione dei dati 
print("")
print(df.head(2))
print("")
print(df.tail(2))
print("")

# Descriscrizione dei dati numerici delle colonne
print("")
print(df.describe())
print("")

# Riporta le descrizione generali di tutte le colonne 
print("")
print(df.info())
print("")

