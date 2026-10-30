# Esercizio omnicomprensivo — Screening diagnostico con scikit-learn

Oct 30, 2026 · @Ore

L'esercizio copre i moduli 1.1–1.7 (Giorno 1) e 2.1, 2.2, 2.4, 2.5 (Giorno 2); il modulo 2.3 (categoriche e dati mancanti) è escluso perché il dataset è tutto numerico e senza valori mancanti.

## Scenario

Un ospedale vuole un sistema di **supporto allo screening** dei tumori al seno. Per ogni paziente dispone di 30 misure numeriche ricavate da un'immagine di un nodulo. Il sistema deve prevedere se il tumore è **maligno** o **benigno**.

Il team clinico pone due vincoli:

- un tumore maligno non riconosciuto è l'errore più grave;
- il numero da comunicare alla direzione deve essere **onesto**, cioè stimato su dati mai usati per addestrare o scegliere il modello.

**Dataset:** `sklearn.datasets.load_breast_cancer`

> ⚠️ Attenzione: in questo dataset `0 = maligno` e `1 = benigno`. La classe che ci interessa individuare è la **0**.

## Mappa degli argomenti trattati

| Modulo | Argomento | Dove compare |
| --- | --- | --- |
| 1.1 | Regole scritte a mano vs ML, modello, parametri, training, inferenza | Punto 1 |
| 1.2 | X e y, tipi di problema, classificazione | Punti 1, 2 |
| 1.3 | venv, librerie, versioni, mappa dei moduli sklearn | Punto 0 |
| 1.4 | `load_*`, Bunch, `as_frame`, `random_state`, `make_*` | Punti 2, 10 |
| 1.5 | API `fit`/`predict`/`score`, `train_test_split`, workflow | Punti 3, 5 |
| 1.6 | KNN, distanza, scelta di k, `kneighbors`, `predict_proba` | Punti 5, 7 |
| 1.7 | Train/validation/test, overfitting, underfitting, curva di complessità | Punti 3, 7, 8 |
| 2.1 | `StandardScaler`, `MinMaxScaler`, modelli che richiedono scaling | Punto 6 |
| 2.4 | Alberi di decisione, Gini, `max_depth`, `export_text` | Punto 8 |
| 2.5 | Matrice di confusione, precision, recall, F1, `stratify`, `DummyClassifier` | Punti 3, 4, 9, 10 |

## Punti dell'esercizio

### 1. Definizione del problema *(1.1, 1.2)*

1. Indica il tipo di apprendimento e di problema (supervisionato/non supervisionato, classificazione/regressione, binaria/multiclasse) e quale colonna è il **target**.

### 2. Esplorazione dei dati *(1.2, 1.4)*

1. Carica il dataset con `as_frame=True`.
2. Stampa:
   - forma di X e di y;
   - nomi delle feature e delle classi;
   - le prime 5 righe;
   - il contenuto di `DESCR` (leggi almeno origine e unità di misura).
3. Controlla quanti campioni ci sono per classe con `value_counts()`: le classi sono bilanciate?
4. Calcola con `describe()` minimo e massimo di tutte le feature. Individua la feature con scala più grande e quella con scala più piccola, e annota perché saranno importanti più avanti.
5. Separa chiaramente `X` e `y`, senza lasciare il target dentro `X`.

### 3. Divisione dei dati *(1.5, 1.7, 2.2, 2.5)*

1. Dividi in **training 60% / validation 20% / test 20%** con due chiamate a `train_test_split`.
2. Usa `random_state=42` e `stratify=y` in entrambe.
3. Stampa le dimensioni dei tre insiemi e la percentuale di maligni in ciascuno.

### 4. Baseline *(2.5)*

1. Addestra un `DummyClassifier(strategy="most_frequent")` e calcola l'accuratezza sul validation set.
2. Calcola anche la recall sui maligni (`pos_label=0`, `zero_division=0`).
3. Commenta: perché questa soglia minima va battuta e perché l'accuratezza da sola può ingannare?

### 5. Primo modello: KNN senza scaling *(1.5, 1.6)*

1. Addestra un `KNeighborsClassifier(n_neighbors=5)` sui dati grezzi, usando la sequenza `fit` → `predict` → `score`.
2. Riporta l'accuratezza su training e su validation.
3. Per un campione del validation set usa `kneighbors` per mostrare distanze, indici e classi dei 5 vicini, e `predict_proba` per mostrare la frazione di voti.
4. Identifica la feature che pesa di più nel calcolo della distanza e spiega perché è un problema.

### 6. Scaling e regola d'oro *(2.1, 2.2)*

1. Applica `StandardScaler` rispettando la regola d'oro:
   - `fit` solo sul training;
   - `transform` su training, validation e test (il test lo scali ora ma non lo usi ancora).
2. Verifica che le colonne del training scalato abbiano media ≈ 0 e deviazione standard ≈ 1, e che quelle del validation **non** abbiano media esattamente 0. Spiega perché è corretto.
3. Riaddestra il KNN con k = 5 sui dati scalati e confronta l'accuratezza di validation con quella del punto 5.
4. Prova `MinMaxScaler` e confronta il risultato con `StandardScaler`.
5. Commenta quali modelli di questo esercizio hanno bisogno dello scaling e quali no.

### 7. Scelta di k e diagnosi del modello *(1.6, 1.7)*

1. Con i dati scalati, per k dispari da 1 a 41 calcola l'accuratezza su training e su validation.
2. Disegna la **curva di complessità** (k sull'asse x, accuratezza sull'asse y, due linee).
3. Individua sul grafico la zona di **overfitting** (k piccolo) e quella di **underfitting** (k grande).
4. Scegli il miglior k **solo guardando il validation set**.

### 8. Secondo modello: albero di decisione *(2.4, 1.7)*

1. Addestra un `DecisionTreeClassifier` per `max_depth` in `[1, 2, 3, 5, 8, None]`, **sui dati non scalati**.
2. Per ogni valore stampa numero di foglie, accuratezza su training e su validation, in una tabella pandas.
3. Scegli la profondità migliore sul validation e giustifica la scelta.
4. Con quella profondità, mostra l'albero con `export_text` (e `plot_tree` se vuoi). Scrivi in italiano le prime due regole che l'albero applica.
5. Calcola a mano l'indice di Gini del nodo radice dalle frazioni delle due classi e verificalo con `albero.tree_.impurity[0]`.
6. Spiega perché per l'albero lo scaling non cambierebbe le decisioni. Per verificarlo, riaddestralo sui dati scalati e confronta.

### 9. Valutazione finale *(2.5, 1.7)*

1. Riaddestra i due modelli scelti (KNN con il k scelto, albero con la profondità scelta) su **training + validation** uniti, con lo scaler rifatto sul nuovo training per il KNN. Poi valutali sul test set.
2. Per ciascun modello e per il Dummy calcola, con la classe positiva = **maligno** (`pos_label=0`):
   - accuratezza, precision, recall, F1;
   - `classification_report` con i nomi delle classi.
3. Disegna la matrice di confusione dei due modelli (`ConfusionMatrixDisplay` o heatmap seaborn).
4. Calcola a mano TP, TN, FP, FN dalla matrice del modello migliore e verifica precision e recall con le formule.
5. Scegli il modello finale secondo il criterio clinico (i falsi negativi sono più gravi) e motiva la scelta in 4–5 righe.
6. Riporta la stima finale che comunicheresti alla direzione e spiega perché è affidabile.

## Regole generali

- Usa **sempre** `random_state=42` (tranne dove l'esercizio chiede di variarlo).
- Il test set compare solo nel punto 9 (e negli esperimenti separati del punto 10).
- Ogni transformer fa `fit` solo sul training.
- Commenta il codice in italiano, spiegando il *perché* e non solo il *cosa*.
- Per ogni grafico: titolo, assi con etichette, legenda dove serve.

## Bonus (facoltativo)

1. Aggiungi il modello `KNeighborsClassifier(weights="distance")` e confrontalo con quello standard.
2. Ripeti la scelta di k con 5 valori di `random_state` diversi nello split e disegna le 5 curve di validation sullo stesso grafico: quanto cambia il k "migliore"? Cosa suggerisce sull'affidabilità di un singolo split? *(anticipazione della cross-validation)*
3. Verifica con `make_moons` che l'albero e il KNN gestiscono confini curvi, e mostra le regioni di decisione con `DecisionBoundaryDisplay`.
