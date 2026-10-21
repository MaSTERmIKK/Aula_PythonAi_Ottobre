import pandas as pd


# caricamento del contenuto del file
df_scv = pd.read_csv("CorsoIt/12_Mercoledi_21/studenti.csv")
print(df_scv)
print("")

# Aggiunta di una colonna
df_scv["Sesso"] = ["F","M","F","F","M","F","F","M","F","M"]
print(df_scv)
print("")

# crea una colonna Promosso riempendola di valori booleani in base alla colonna voto
df_scv["promosso"] = df_scv["voto"] >= 6
print(df_scv)
print("")

# stampa la media dei voti
print(df_scv["voto"].mean())
print("")
# stampa il valore massimo dei voti
print(df_scv["voto"].max())
print("")

# stampa di una condizione bolleana
print(df_scv[df_scv["voto"] > 7])
print("")

# Salvare il DataFrame in un nuovo CSV
df_scv.to_csv("CorsoIt/12_Mercoledi_21/studenti_aggiornato.csv", index=False)
