"""
VARIABILI IN PYTHON

- int
- float
- str
- bool
- assegnazione
- type()
- casting
- operazioni
- assegnazione multipla
- input
- None
"""


# ==============================================================
# 1. VARIABILI INTERE
# ==============================================================

eta = 25
anno = 2026

print("Età:", eta)
print("Anno:", anno)
print()


# ==============================================================
# 2. VARIABILI FLOAT
# ==============================================================

prezzo = 19.99
temperatura = 22.5

print("Prezzo:", prezzo)
print("Temperatura:", temperatura)
print()


# ==============================================================
# 3. STRINGHE
# ==============================================================

nome = "Mario"
cognome = "Rossi"

print("Nome:", nome)
print("Cognome:", cognome)

nome_completo = nome + " " + cognome

print("Nome completo:", nome_completo)
print()


# ==============================================================
# 4. BOOLEANI
# ==============================================================

attivo = True
amministratore = False

print("Attivo:", attivo)
print("Amministratore:", amministratore)
print()


# ==============================================================
# 5. TYPE()
# ==============================================================

numero = 10
decimale = 10.5
testo = "Python"
stato = True

print(type(numero))
print(type(decimale))
print(type(testo))
print(type(stato))
print()


# ==============================================================
# 6. MODIFICA DI UNA VARIABILE
# ==============================================================

punteggio = 10

print("Prima:", punteggio)

punteggio = 20

print("Dopo:", punteggio)
print()


# ==============================================================
# 7. TIPIZZAZIONE DINAMICA
# ==============================================================

dato = 100
print(dato, type(dato))

dato = "Ciao"
print(dato, type(dato))

dato = True
print(dato, type(dato))

print()


# ==============================================================
# 8. OPERAZIONI TRA VARIABILI
# ==============================================================

a = 10
b = 3

print("Somma:", a + b)
print("Sottrazione:", a - b)
print("Moltiplicazione:", a * b)
print("Divisione:", a / b)
print("Divisione intera:", a // b)
print("Resto:", a % b)
print("Potenza:", a ** b)

print()


# ==============================================================
# 9. OPERATORI DI ASSEGNAZIONE
# ==============================================================

numero = 10

numero += 5
print("+= :", numero)

numero -= 3
print("-= :", numero)

numero *= 2
print("*= :", numero)

numero /= 4
print("/= :", numero)

print()


# ==============================================================
# 10. ASSEGNAZIONE MULTIPLA
# ==============================================================

x, y, z = 10, 20, 30

print("x:", x)
print("y:", y)
print("z:", z)

print()


# ==============================================================
# 11. STESSO VALORE A PIÙ VARIABILI
# ==============================================================

a = b = c = 100

print(a)
print(b)
print(c)

print()


# ==============================================================
# 12. SCAMBIO DI VARIABILI
# ==============================================================

a = 10
b = 20

print("Prima:", a, b)

a, b = b, a

print("Dopo:", a, b)

print()


# ==============================================================
# 13. CASTING
# ==============================================================

testo = "25"

numero = int(testo)
decimale = float(testo)

print(numero, type(numero))
print(decimale, type(decimale))

numero = 100
testo = str(numero)

print(testo, type(testo))

print()


# ==============================================================
# 14. F-STRING
# ==============================================================

nome = "Anna"
eta = 28

messaggio = f"{nome} ha {eta} anni"

print(messaggio)
print()


# ==============================================================
# 15. NONE
# ==============================================================

risultato = None

print("Risultato:", risultato)
print("Tipo:", type(risultato))

print()


# ==============================================================
# 16. COSTANTI PER CONVENZIONE
# ==============================================================

PI_GRECO = 3.14159
MAX_UTENTI = 100

print("PI:", PI_GRECO)
print("Massimo utenti:", MAX_UTENTI)

print()


# ==============================================================
# 17. INPUT UTENTE
# ==============================================================

nome = input("Inserisci il tuo nome: ")

print("Ciao", nome)

print()


# ==============================================================
# 18. INPUT NUMERICO
# ==============================================================

eta = int(input("Inserisci la tua età: "))

print("Hai", eta, "anni")

print()


# ==============================================================
# 19. ESEMPIO PRATICO
# ==============================================================

prodotto = "Mouse"
prezzo = 25.50
quantita = 3

totale = prezzo * quantita

print("Prodotto:", prodotto)
print("Prezzo:", prezzo)
print("Quantità:", quantita)
print("Totale:", totale)
