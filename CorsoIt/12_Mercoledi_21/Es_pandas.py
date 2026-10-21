import pandas as pd

# 1. Caricare il CSV in un DataFrame
df = pd.read_csv("vendite.csv") # csv ipotetico
print(df)


# 2. Aggiungere la colonna TotaleVendite
df["TotaleVendite"] = df["Quantita"] * df["PrezzoUnitario"]
print(df)


# 3. Raggruppare per prodotto e sommare le vendite
totali = df.groupby("Prodotto")["TotaleVendite"].sum()
print(totali)


# 4. Trovare il prodotto più venduto per quantità
quantita = df.groupby("Prodotto")["Quantita"].sum()

prodotto = quantita.idxmax()
totale = quantita.max()

print("Prodotto più venduto:", prodotto)
print("Quantità venduta:", totale)


# 5. Trovare la città con maggiori vendite
citta = df.groupby("Citta")["TotaleVendite"].sum()
print(citta.idxmax())


# 6. Creare un DataFrame con vendite superiori a 1000 euro
vendite_alte = df[df["TotaleVendite"] > 1000]
print(vendite_alte)


# 7. EXTRA


# 8. Contare il numero di vendite per città
conteggio = df["Citta"].value_counts()
print(conteggio)