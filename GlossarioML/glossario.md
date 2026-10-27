# Glossario del corso — Machine Learning con scikit-learn e TensorFlow/Keras

Concetti ordinati per giornata e modulo in cui vengono spiegati. Le definizioni coincidono con quelle usate nelle slide.

---

## Giorno 1 — Fondamenti di Machine Learning e primo modello

### 1.1 Cos'è il Machine Learning
| Termine | Definizione |
|---|---|
| Intelligenza Artificiale (AI) | Insieme delle tecniche che permettono a una macchina di svolgere compiti che normalmente richiedono intelligenza umana. |
| Machine Learning (ML) | Parte dell'AI in cui il computer impara dai dati invece di seguire regole scritte a mano. |
| Deep Learning (DL) | Parte del ML basata su reti neurali con molti strati. |
| Programmazione classica | Approccio in cui il programmatore scrive le regole: regole + dati → risposte. |
| Algoritmo di apprendimento | Procedura che cerca nei dati la regola migliore (la "ricetta"). |
| Modello | Risultato dell'apprendimento: funzione matematica che trasforma un input in un output. |
| Parametri (pesi) | Valori interni al modello regolati durante l'addestramento (es. una soglia, i coefficienti di una retta). |
| Addestramento (training) | Processo in cui l'algoritmo regola i parametri per far sbagliare il modello il meno possibile sugli esempi. |
| Inferenza / predizione | Uso del modello addestrato su dati nuovi, mai visti. |
| Pattern | Regolarità presente nei dati che il modello cerca di cogliere. |

### 1.2 Dati e tipi di apprendimento
| Termine | Definizione |
|---|---|
| Dataset | Insieme di dati organizzato come tabella. |
| Campione (osservazione, istanza) | Una riga del dataset: un singolo caso. |
| Feature (caratteristica, variabile indipendente) | Una colonna che descrive il campione e viene usata come input. |
| Target (etichetta, label, variabile dipendente) | La colonna da prevedere. |
| X | Matrice 2D delle feature, di forma `(n_campioni, n_feature)`. |
| y | Vettore 1D del target, uno per campione. |
| Dati etichettati | Dati per cui si conosce la risposta corretta (esiste y). |
| Apprendimento supervisionato | Il modello impara la relazione X → y da dati etichettati. |
| Classificazione | Problema supervisionato in cui y è una categoria. |
| Classificazione binaria / multiclasse | Classificazione con 2 classi / con più di 2 classi. |
| Regressione | Problema supervisionato in cui y è un numero continuo. |
| Apprendimento non supervisionato | Il modello cerca strutture in dati senza y. |
| Clustering | Raggruppamento di campioni simili senza gruppi predefiniti. |
| Riduzione della dimensionalità | Riassumere molte feature in poche conservando l'informazione essenziale. |
| Apprendimento per rinforzo | Un agente impara per tentativi ed errori a scegliere azioni che massimizzano una ricompensa. |
| Agente / ambiente / ricompensa | Nel rinforzo: chi decide / il mondo in cui agisce / il segnale positivo o negativo che riceve. |

### 1.3 Librerie, setup e mappa di scikit-learn
| Termine | Definizione |
|---|---|
| scikit-learn | Libreria Python per il ML classico su dati tabellari, con API uniforme. Si installa come `scikit-learn`, si importa come `sklearn`. |
| TensorFlow / Keras | Libreria di Google per il deep learning; Keras è la sua interfaccia di alto livello. |
| PyTorch | Libreria di deep learning molto usata nella ricerca, con grafo computazionale dinamico. |
| Ambiente virtuale (venv) | Installazione Python isolata con le proprie librerie, una per progetto. |
| pip | Gestore dei pacchetti Python: installa, aggiorna e rimuove librerie. |
| Dipendenza | Libreria necessaria al funzionamento di un'altra (es. NumPy e SciPy per scikit-learn). |
| requirements.txt | File con l'elenco delle librerie e delle versioni esatte di un progetto. |
| Modulo di scikit-learn | Sotto-pacchetto che raggruppa strumenti dello stesso tipo (es. `sklearn.metrics`). |

### 1.4 Dataset in scikit-learn
| Termine | Definizione |
|---|---|
| `load_*` | Funzioni che caricano piccoli dataset inclusi nella libreria. |
| `fetch_*` | Funzioni che scaricano dataset più grandi da internet al primo utilizzo. |
| `make_*` | Funzioni che generano dataset sintetici con caratteristiche controllate. |
| Bunch | Oggetto simile a un dizionario restituito da `load_*`: contiene `data`, `target`, `feature_names`, `target_names`, `DESCR`. |
| `return_X_y` / `as_frame` | Opzioni per ottenere direttamente `(X, y)` / oggetti pandas. |
| Classi bilanciate | Situazione in cui ogni classe ha un numero simile di campioni. |
| Confine non lineare | Separazione tra classi che richiede una linea curva (es. `make_moons`). |
| Seme casuale (`random_state`) | Numero iniziale del generatore pseudo-casuale: stesso seme → stessi risultati (riproducibilità). |

### 1.5 API di scikit-learn e workflow
| Termine | Definizione |
|---|---|
| Estimator | Classe di scikit-learn che implementa un algoritmo; il modello ne è un'istanza. |
| `fit(X, y)` | Metodo che addestra il modello sui dati. |
| `predict(X)` | Metodo che restituisce le predizioni per nuovi dati. |
| `score(X, y)` | Metodo che restituisce un punteggio di prestazione (accuratezza per i classificatori). |
| Iperparametro | Impostazione scelta dall'utente prima dell'addestramento (es. `n_neighbors`). |
| Attributo appreso | Valore calcolato da `fit`, con nome che finisce in `_` (es. `classes_`, `n_features_in_`). |
| Training set | Parte dei dati usata per addestrare il modello. |
| Test set | Parte dei dati tenuta da parte per valutare il modello su dati mai visti. |
| `train_test_split` | Funzione che divide X e y in training e test; restituisce X_train, X_test, y_train, y_test. |
| `test_size` | Frazione dei dati assegnata al test set (default 0.25). |
| Shuffle | Mescolamento casuale delle righe prima della divisione. |
| Accuratezza (accuracy) | Previsioni corrette / previsioni totali; va da 0 a 1. |
| `accuracy_score` | Funzione di `sklearn.metrics` che calcola l'accuratezza. |
| Workflow ML | Sequenza: dati → preprocessing → divisione → scelta modello → fit → predict → valutazione → ottimizzazione. |

### 1.6 K-Nearest Neighbors
| Termine | Definizione |
|---|---|
| K-Nearest Neighbors (KNN) | Algoritmo che assegna a un punto la classe più frequente tra i suoi k vicini più prossimi. |
| `n_neighbors` (k) | Numero di vicini considerati (default 5). |
| Distanza euclidea | Distanza in linea retta tra due punti: radice della somma delle differenze al quadrato. |
| Voto di maggioranza | Scelta della classe più frequente tra i vicini. |
| Lazy learning | Apprendimento "pigro": `fit` memorizza i dati e il calcolo avviene in `predict`. |
| `weights` | `"uniform"`: ogni vicino vale uguale; `"distance"`: i vicini più vicini pesano di più. |
| `kneighbors` | Metodo che restituisce distanze e indici dei vicini di un punto. |
| `predict_proba` | Metodo che restituisce la probabilità stimata di ogni classe. |
| `KNeighborsRegressor` | Versione di KNN per la regressione: prevede la media dei valori dei vicini. |
| Regione / confine di decisione | Area del piano assegnata a una classe / linea che separa le regioni. |

### 1.7 Generalizzazione
| Termine | Definizione |
|---|---|
| Generalizzazione | Capacità del modello di funzionare bene su dati nuovi. |
| Errore di training / di test | Errore misurato sui dati di addestramento / su dati mai visti. |
| Overfitting | Il modello memorizza i dati di training (anche il rumore): training alto, test basso. |
| Underfitting | Il modello è troppo semplice: punteggi bassi sia su training sia su test. |
| Rumore | Variazioni casuali o errori nei dati che non rappresentano la regola generale. |
| Bias | Errore dovuto a ipotesi troppo semplici; bias alto → underfitting. |
| Varianza | Sensibilità del modello ai dati specifici di training; varianza alta → overfitting. |
| Validation set | Parte dei dati usata per scegliere gli iperparametri. |
| Curva di complessità | Grafico delle prestazioni su training e test al variare di un iperparametro di complessità. |
| Cross-validation (anticipazione) | Tecnica che ripete la divisione dei dati più volte per una stima più stabile (giorno 4). |

---

## Giorno 2 — Preprocessing e valutazione dei classificatori

### 2.1 Scaling delle feature
| Termine | Definizione |
|---|---|
| Scaling | Trasformazione che porta le feature su scale confrontabili. |
| Media | Somma dei valori diviso il loro numero. |
| Deviazione standard | Quanto, in media, i valori si allontanano dalla media. |
| Varianza | Deviazione standard al quadrato. |
| Standardizzazione (`StandardScaler`) | `z = (x − media) / dev. standard`: ogni feature ha media 0 e dev. standard 1. |
| Normalizzazione (`MinMaxScaler`) | `(x − min) / (max − min)`: ogni feature va da 0 a 1. |
| Outlier | Valore anomalo, molto lontano dagli altri. |
| `RobustScaler` | Scaler basato su mediana e intervallo interquartile, poco sensibile agli outlier. |
| Transformer | Oggetto di scikit-learn che trasforma i dati (`fit` + `transform`). |
| `fit` / `transform` / `fit_transform` | Impara le statistiche / le applica / fa entrambe le cose. |
| `inverse_transform` | Riporta i dati trasformati alla scala originale. |

### 2.2 Data leakage
| Termine | Definizione |
|---|---|
| Data leakage | Il modello riceve in addestramento informazioni che non dovrebbe avere, producendo stime troppo ottimistiche. |
| Regola d'oro del preprocessing | Prima lo split; `fit` di ogni transformer solo sul training; `transform` su training e test. |
| Target leakage | Una feature contiene, anche indirettamente, la risposta da prevedere. |
| Leakage temporale | Uso di dati futuri per prevedere il passato. |
| Selezione delle feature (`SelectKBest`) | Scelta delle k colonne più legate al target; anch'essa va fatta solo sul training. |

### 2.3 Variabili categoriche e dati mancanti
| Termine | Definizione |
|---|---|
| Variabile nominale | Categoria senza ordine (città, colore). |
| Variabile ordinale | Categoria con un ordine naturale (taglia S/M/L). |
| `LabelEncoder` | Converte le etichette del target in interi 0…n−1. |
| `OrdinalEncoder` | Converte feature ordinali in interi secondo l'ordine indicato con `categories`. |
| One-hot encoding (`OneHotEncoder`) | Crea una colonna 0/1 per ogni categoria di una feature nominale. |
| `handle_unknown="ignore"` | Le categorie mai viste nel training diventano tutte 0 invece di generare errore. |
| Matrice sparsa | Formato compatto che memorizza solo i valori diversi da zero. |
| `pd.get_dummies` | Equivalente pandas del one-hot, che però non ricorda le categorie del training. |
| Valore mancante (NaN) | Dato assente in una cella; si contano con `isna().sum()`. |
| Imputazione | Sostituzione dei valori mancanti con un valore stimato. |
| `SimpleImputer` | Imputer con strategie `mean`, `median`, `most_frequent`, `constant`. |
| Mediana | Valore centrale dei dati ordinati; robusta agli outlier. |
| `add_indicator` | Aggiunge una colonna 0/1 che segnala dove il valore era mancante. |
| `ColumnTransformer` | Applica transformer diversi a gruppi di colonne diversi e unisce i risultati. |

### 2.4 Alberi di decisione
| Termine | Definizione |
|---|---|
| Albero di decisione | Modello che prevede tramite una sequenza di domande sì/no sulle feature. |
| Nodo radice / interno / foglia | Prima domanda / domande intermedie / nodo finale con la predizione. |
| Split | Divisione di un nodo in due in base a una feature e una soglia. |
| Profondità | Numero di domande dalla radice alla foglia più lontana. |
| Purezza / impurità | Quanto un nodo contiene campioni di una sola classe / quanto è "mescolato". |
| Indice di Gini | `1 − Σ pᵢ²`: 0 per un nodo puro, cresce con il disordine. |
| Entropia | Misura alternativa dell'impurità, dalla teoria dell'informazione. |
| Algoritmo greedy | Sceglie a ogni passo l'opzione migliore del momento senza tornare indietro. |
| `max_depth`, `min_samples_split`, `min_samples_leaf` | Iperparametri che limitano la crescita dell'albero e riducono l'overfitting. |
| `export_text` / `plot_tree` | Visualizzazione delle regole dell'albero in testo / grafico. |
| `DecisionTreeRegressor` | Albero per la regressione: ogni foglia prevede la media dei suoi campioni. |

### 2.5 Metriche di classificazione
| Termine | Definizione |
|---|---|
| Classe positiva | La classe che vogliamo individuare (malato, frode, spam). |
| TP / TN | Veri positivi / veri negativi: previsioni corrette. |
| FP (falso allarme) / FN (caso mancato) | Negativo previsto come positivo / positivo previsto come negativo. |
| Matrice di confusione | Tabella reale × previsto; in scikit-learn righe = reali, colonne = previste. |
| Precision | TP / (TP + FP): affidabilità delle previsioni positive. |
| Recall (sensibilità) | TP / (TP + FN): quota di positivi reali individuati. |
| F1-score | Media armonica di precision e recall. |
| Classi sbilanciate | Una classe è molto più frequente delle altre; l'accuratezza diventa fuorviante. |
| Support | Numero di campioni reali di una classe nel test set. |
| Macro avg / weighted avg | Media semplice delle metriche per classe / media pesata per il support. |
| `classification_report` | Report testuale con precision, recall, F1 e support per classe. |
| `pos_label` | Parametro che indica quale etichetta è la classe positiva. |
| `zero_division` | Valore restituito quando una metrica richiederebbe una divisione per zero. |
| Split stratificato (`stratify=y`) | Divisione che mantiene le proporzioni delle classi in training e test. |
| `DummyClassifier` | Modello di riferimento che ignora le feature; soglia minima da superare. |
| Heatmap | Grafico a celle colorate, usato per visualizzare la matrice di confusione. |

---

## Giorno 3 — Modelli supervisionati: regressione, modelli lineari e SVM

### 3.1 Regressione lineare
| Termine | Definizione |
|---|---|
| Regressione lineare | Modello che prevede un numero come combinazione lineare delle feature: `ŷ = w₁x₁ + … + wₙxₙ + b`. |
| ŷ (y cappello) | Valore previsto dal modello. |
| Coefficiente (`coef_`) | Variazione di ŷ quando la feature aumenta di 1, a parità delle altre. |
| Intercetta (`intercept_`) | Valore di ŷ quando tutte le feature valgono 0. |
| Regressione semplice / multipla | Con una sola feature / con più feature. |
| Iperpiano | Generalizzazione della retta e del piano a più dimensioni. |
| Residuo | Differenza tra valore reale e previsto: `y − ŷ`. |
| Minimi quadrati | Metodo che sceglie i coefficienti minimizzando la somma dei residui al quadrato. |
| `PolynomialFeatures` | Transformer che aggiunge le potenze delle feature (x², x³…) per modellare curve. |
| `degree` | Grado massimo del polinomio; troppo alto causa overfitting. |

### 3.2 Metriche di regressione
| Termine | Definizione |
|---|---|
| MAE | Errore assoluto medio: media di \|y − ŷ\|, nella stessa unità del target. |
| MSE | Errore quadratico medio: media di (y − ŷ)²; penalizza molto gli errori grandi. |
| RMSE | Radice dell'MSE: nella stessa unità del target. |
| R² (coefficiente di determinazione) | Frazione della variabilità di y spiegata dal modello rispetto al prevedere sempre la media; 1 perfetto, 0 come la media, negativo peggio. |
| `root_mean_squared_error` | Funzione per l'RMSE (sostituisce il vecchio `squared=False`). |
| `DummyRegressor` | Modello di riferimento che prevede sempre la media (o mediana) del training. |
| Analisi dei residui | Studio grafico degli errori per scoprire dove il modello sbaglia sistematicamente. |

### 3.3 Regolarizzazione
| Termine | Definizione |
|---|---|
| Regolarizzazione | Penalità sulla grandezza dei coefficienti aggiunta all'addestramento per ridurre l'overfitting. |
| `alpha` | Forza della regolarizzazione nei regressori lineari: più è grande, più i coefficienti sono schiacciati. |
| Ridge (L2) | Regolarizzazione che penalizza la somma dei quadrati dei coefficienti; li riduce tutti. |
| Lasso (L1) | Regolarizzazione che penalizza la somma dei valori assoluti; azzera alcuni coefficienti (selezione delle feature). |
| ElasticNet | Combinazione di L1 e L2, regolata da `l1_ratio`. |
| Feature correlate (multicollinearità) | Feature che contengono informazioni molto simili; rendono instabili i coefficienti. |
| C (nei classificatori) | Inverso della forza di regolarizzazione: C piccolo = regolarizzazione forte. |

### 3.4 Regressione logistica
| Termine | Definizione |
|---|---|
| Regressione logistica | Classificatore lineare che stima la probabilità di appartenenza a una classe. |
| Funzione sigmoide (logistica) | `σ(z) = 1 / (1 + e⁻ᶻ)`: trasforma qualsiasi numero in un valore tra 0 e 1. |
| Soglia di decisione | Probabilità oltre la quale si assegna la classe positiva (default 0.5). |
| Classificatore lineare | Modello il cui confine di decisione è una retta/iperpiano. |
| Log loss (entropia incrociata) | Funzione di errore che punisce molto le previsioni sicure e sbagliate. |
| Solver | Algoritmo di ottimizzazione che cerca i coefficienti per tentativi successivi. |
| Convergenza / `ConvergenceWarning` | Il solver ha trovato una soluzione stabile / avviso che non ci è riuscito entro `max_iter`. |
| Softmax | Generalizzazione della sigmoide a più classi: probabilità per classe che sommano a 1. |
| `decision_function` | Punteggio del modello prima della trasformazione in probabilità. |
| `l1_ratio` | Dalla versione 1.8, sceglie il tipo di penalità della regressione logistica (0 = L2, 1 = L1). |

### 3.5 Support Vector Machine
| Termine | Definizione |
|---|---|
| Support Vector Machine (SVM) | Modello che separa le classi con l'iperpiano di margine massimo. |
| Margine | Fascia libera tra l'iperpiano e i punti più vicini delle due classi. |
| Vettori di supporto | Punti sul bordo o dentro il margine: gli unici che determinano il confine. |
| Margine morbido | Margine che tollera alcuni punti dalla parte sbagliata, pagando una penalità regolata da C. |
| Kernel | Funzione che misura la somiglianza tra due punti come se fossero in uno spazio di dimensione maggiore. |
| Kernel trick | Uso di un kernel per ottenere confini non lineari senza calcolare esplicitamente le nuove coordinate. |
| Kernel linear / poly / rbf / sigmoid | Nessuna trasformazione / polinomiale / gaussiano (default) / simile a una rete neurale. |
| gamma | Raggio d'influenza di ogni punto nei kernel rbf e poly: grande → confini frastagliati (overfitting). |
| `LinearSVC` | Implementazione veloce della SVM lineare per grandi dataset. |
| SVR | Versione della SVM per la regressione. |

---

## Giorno 4 — Ensemble, validazione incrociata, ottimizzazione e Pipeline

### 4.1 Metodi ensemble
| Termine | Definizione |
|---|---|
| Ensemble | Modello che combina le previsioni di molti modelli. |
| Bootstrap | Estrazione casuale con reinserimento di un nuovo dataset della stessa dimensione dell'originale. |
| Bagging | Addestramento in parallelo di più modelli su dataset bootstrap e aggregazione delle previsioni; riduce la varianza. |
| Random Forest | Bagging di alberi in cui a ogni split si considera solo un sottoinsieme casuale di feature. |
| `n_estimators` | Numero di modelli (alberi) dell'ensemble. |
| `max_features` | Numero di feature valutate a ogni split (default `"sqrt"`; `"auto"` è stato rimosso). |
| Out-of-bag (OOB) | Campioni rimasti fuori dal bootstrap di un albero; usati per una stima di validazione gratuita (`oob_score`). |
| Boosting | Addestramento in sequenza di modelli, ognuno focalizzato sugli errori dei precedenti; riduce il bias. |
| Weak learner | Modello debole (es. albero piccolo), poco migliore del caso, usato come base del boosting. |
| AdaBoost | Boosting che aumenta il peso dei campioni classificati male. |
| Gradient Boosting | Boosting in cui ogni nuovo albero impara a correggere gli errori residui del modello attuale. |
| `learning_rate` | Peso del contributo di ogni nuovo albero nel boosting; più è basso, più alberi servono. |
| `subsample` | Frazione di campioni usata da ogni albero nel gradient boosting. |
| HistGradientBoosting | Versione veloce del gradient boosting, adatta a dataset grandi e con valori mancanti. |
| `feature_importances_` | Contributo di ogni feature alla riduzione dell'impurità negli alberi; somma 1. |
| Permutation importance | Importanza misurata come peggioramento del modello quando si mescola una feature. |

### 4.2 Parametri, iperparametri e bias-varianza
| Termine | Definizione |
|---|---|
| `get_params` / `set_params` | Lettura / modifica degli iperparametri di un modello. |
| Compromesso bias-varianza | Aumentando la complessità il bias scende e la varianza sale; l'errore totale è minimo nel mezzo. |
| Rumore irriducibile | Parte casuale dei dati che nessun modello può eliminare. |
| Curva di validazione | Punteggi di training e validation al variare di un iperparametro. |
| Curva di apprendimento (learning curve) | Punteggi di training e validation al variare del numero di campioni di training. |

### 4.3 Cross-validation
| Termine | Definizione |
|---|---|
| Cross-validation (validazione incrociata) | Valutazione ripetuta su più divisioni dei dati per una stima più affidabile. |
| Fold | Ciascuna delle k parti in cui si dividono i dati nella cross-validation. |
| K-Fold | Ogni fold fa da validation una volta, gli altri k−1 da training; si ottengono k punteggi. |
| Stratified K-Fold | K-Fold che mantiene le proporzioni delle classi in ogni fold. |
| LeaveOneOut | Cross-validation con un solo campione in validation per volta. |
| TimeSeriesSplit | Cross-validation per dati temporali: si valida sempre su periodi successivi al training. |
| `cross_val_score` | Funzione che restituisce i k punteggi di una metrica. |
| `cross_validate` | Come `cross_val_score` ma con più metriche, tempi e punteggi di training. |
| `scoring` | Nome della metrica usata nella valutazione o nella ricerca. |
| Metriche negative (`neg_…`) | Errori espressi con il segno meno per rispettare la convenzione "più alto è meglio". |

### 4.4 Ricerca degli iperparametri
| Termine | Definizione |
|---|---|
| Ricerca degli iperparametri (tuning) | Processo automatico di scelta degli iperparametri migliori. |
| `GridSearchCV` | Prova tutte le combinazioni di una griglia, valutandole con la cross-validation. |
| `param_grid` | Dizionario (o lista di dizionari) con i valori da provare per ogni iperparametro. |
| `refit` | Riaddestramento del modello migliore su tutto il training al termine della ricerca. |
| `best_params_` / `best_score_` / `best_estimator_` | Combinazione migliore / suo punteggio medio in CV / modello migliore riaddestrato. |
| `cv_results_` | Tabella con i risultati di tutte le combinazioni provate. |
| `RandomizedSearchCV` | Prova `n_iter` combinazioni estratte a caso da liste o distribuzioni. |
| Distribuzione di probabilità | Regola con cui si estraggono valori casuali (`randint`, `uniform`, `loguniform`). |
| `loguniform` | Distribuzione uniforme sugli ordini di grandezza; adatta a C, gamma, alpha, learning_rate. |
| `n_jobs` | Numero di processori usati in parallelo (−1 = tutti). |

### 4.5 Pipeline
| Termine | Definizione |
|---|---|
| Pipeline | Oggetto che concatena transformer e modello finale e si usa come un unico modello. |
| `make_pipeline` | Crea una Pipeline assegnando i nomi dei passaggi in automatico. |
| Passaggio (step) | Ogni coppia (nome, oggetto) della Pipeline. |
| `passo__parametro` | Sintassi con doppio underscore per indicare un iperparametro di un passaggio nella ricerca. |
| `named_steps` | Accesso ai singoli passaggi addestrati di una Pipeline. |
| `joblib.dump` / `joblib.load` | Salvataggio / caricamento su file di un modello o di una Pipeline. |

---

## Giorno 5 — Apprendimento non supervisionato

### 5.1 Riduzione della dimensionalità e PCA
| Termine | Definizione |
|---|---|
| Dimensionalità | Numero di feature di un dataset. |
| Maledizione della dimensionalità | Con molte feature i dati diventano radi e le distanze perdono significato. |
| Selezione delle feature | Tenere alcune feature originali e scartare le altre. |
| Estrazione delle feature | Creare nuove feature combinando quelle originali. |
| PCA (Analisi delle Componenti Principali) | Tecnica che trova nuovi assi ortogonali ordinati per varianza e proietta i dati sui primi k. |
| Componente principale | Nuovo asse, combinazione lineare delle feature originali (`components_`). |
| Ortogonale | Perpendicolare: componenti che non ripetono la stessa informazione. |
| Varianza spiegata (`explained_variance_ratio_`) | Frazione della varianza totale conservata da ogni componente. |
| Scree plot | Grafico della varianza spiegata per componente, usato per scegliere quante tenerne. |
| SVD | Decomposizione ai valori singolari: tecnica di algebra lineare usata per calcolare la PCA. |
| Ricostruzione (`inverse_transform`) | Ritorno approssimato allo spazio originale dalle componenti tenute. |
| `IncrementalPCA` | PCA che elabora i dati a blocchi, per dataset che non entrano in memoria. |

### 5.2 Kernel PCA, t-SNE, Truncated SVD
| Termine | Definizione |
|---|---|
| Prodotto scalare | Somma dei prodotti delle feature corrispondenti di due campioni (`x·y`). |
| `KernelPCA` | PCA applicata nello spazio di un kernel; coglie strutture non lineari. |
| t-SNE | Tecnica non lineare per visualizzare dati in 2D/3D preservando le vicinanze locali; non ha `transform`. |
| `perplexity` | Iperparametro di t-SNE: circa il numero di vicini considerati. |
| TF-IDF | Rappresentazione numerica dei testi che pesa ogni parola per frequenza nel documento e rarità negli altri. |
| `stop_words` | Parole molto comuni e senza contenuto da ignorare nell'analisi dei testi. |
| `TruncatedSVD` | Riduzione della dimensionalità senza centrare i dati, adatta alle matrici sparse. |
| LSA (Latent Semantic Analysis) | Uso della TruncatedSVD sui testi per far emergere argomenti latenti. |

### 5.3 Clustering
| Termine | Definizione |
|---|---|
| Cluster | Gruppo di campioni simili tra loro e diversi da quelli degli altri gruppi. |
| K-Means | Algoritmo che assegna ogni punto al centroide più vicino e sposta i centroidi nella media del loro gruppo, fino a convergenza. |
| Centroide (`cluster_centers_`) | Punto medio di un cluster. |
| `k-means++` | Inizializzazione che sceglie centroidi iniziali distanti tra loro. |
| `n_init` | Numero di ripetizioni di K-Means con centroidi iniziali diversi. |
| Inerzia (`inertia_`) | Somma delle distanze al quadrato dei punti dal proprio centroide. |
| Metodo del gomito | Scelta di k nel punto in cui l'inerzia smette di scendere rapidamente. |
| Coefficiente di silhouette | `(b − a) / max(a, b)`: misura quanto un punto è vicino al suo cluster e lontano dagli altri (−1…1). |
| Clustering agglomerativo (gerarchico) | Parte da un cluster per punto e unisce progressivamente i più vicini. |
| Linkage (ward, complete, average, single) | Criterio per misurare la distanza tra due cluster. |
| Dendrogramma | Diagramma ad albero della sequenza di unioni del clustering gerarchico. |
| DBSCAN | Clustering basato sulla densità: trova cluster di forma qualsiasi e marca il rumore. |
| `eps` / `min_samples` | Raggio dell'intorno / numero minimo di punti nell'intorno per un punto centrale. |
| Punto centrale / di bordo / rumore | Punto in zona densa / vicino a un punto centrale ma non denso / isolato (etichetta −1). |
| Adjusted Rand Index (ARI) | Somiglianza tra cluster ed etichette vere: 1 identici, circa 0 casuali. |
| Omogeneità / completezza / V-measure | Ogni cluster contiene una sola classe / ogni classe sta in un solo cluster / loro media armonica. |

---

## Giorno 6 — Reti neurali e TensorFlow/Keras: fondamenti

### 6.1 Dal neurone alla rete neurale
| Termine | Definizione |
|---|---|
| Rete neurale | Modello composto da molti neuroni artificiali organizzati in strati. |
| Neurone artificiale | Unità che calcola una somma pesata degli input più un bias e applica una funzione di attivazione. |
| Peso | Coefficiente che indica quanto conta un input per un neurone; viene imparato. |
| Bias | Valore aggiunto alla somma pesata, simile all'intercetta; viene imparato. |
| Funzione di attivazione | Funzione non lineare applicata all'uscita del neurone. |
| ReLU | `max(0, z)`: attivazione di default per gli strati nascosti. |
| Sigmoide | Attivazione con uscita tra 0 e 1, per la classificazione binaria. |
| Tanh | Attivazione con uscita tra −1 e 1. |
| Softmax | Attivazione di uscita multiclasse: probabilità che sommano a 1. |
| Strato (layer) di input / nascosto / di output | Rappresenta le feature / elabora l'informazione / produce la previsione. |
| Strato denso (Dense, fully connected) | Strato in cui ogni neurone è collegato a tutti i neuroni dello strato precedente. |
| Deep learning | Machine learning con reti neurali a molti strati nascosti. |
| Forward pass | Calcolo della previsione strato dopo strato, dall'input all'output. |
| Dati non strutturati | Dati non organizzati in tabella: immagini, audio, testo. |

### 6.2 Come impara una rete neurale
| Termine | Definizione |
|---|---|
| Funzione di perdita (loss) | Numero che misura l'errore della rete; l'addestramento cerca di minimizzarlo. |
| Binary crossentropy | Loss per la classificazione binaria (log loss). |
| Categorical crossentropy | Loss multiclasse: −log della probabilità assegnata alla classe corretta. |
| Gradiente | Pendenza della loss rispetto a ciascun peso: indica come cambia l'errore modificando il peso. |
| Discesa del gradiente | Aggiornamento dei pesi nella direzione opposta al gradiente: `w = w − lr · gradiente`. |
| Learning rate | Lunghezza del passo di aggiornamento: troppo piccolo è lento, troppo grande diverge. |
| Divergenza | La loss cresce invece di diminuire perché i passi sono troppo grandi. |
| Backpropagation | Calcolo efficiente di tutti i gradienti procedendo dall'output verso l'input. |
| Differenziazione automatica | Calcolo automatico delle derivate da parte della libreria. |
| Batch (`batch_size`) | Gruppo di esempi usato per un aggiornamento dei pesi. |
| Iterazione (step) | Un aggiornamento dei pesi, cioè un batch elaborato. |
| Epoca | Un passaggio completo su tutto il training set. |
| Ottimizzatore | Algoritmo che aggiorna i pesi: SGD, SGD con momentum, RMSProp, Adam. |
| Momentum | Tecnica che aggiunge "inerzia" agli aggiornamenti per ridurre le oscillazioni. |
| Adam | Ottimizzatore con momentum e learning rate adattivo per ogni peso; scelta di default. |

### 6.3 TensorFlow
| Termine | Definizione |
|---|---|
| TensorFlow | Libreria open-source di Google per il calcolo numerico e il deep learning su CPU, GPU e TPU. |
| Tensore | Array multidimensionale di numeri, struttura dati di base di TensorFlow. |
| Rango (`ndim`) | Numero di dimensioni di un tensore: 0 scalare, 1 vettore, 2 matrice, … |
| Shape | Dimensione del tensore lungo ogni asse. |
| dtype | Tipo dei numeri del tensore (le reti usano `float32`). |
| `tf.constant` / `tf.Variable` | Tensore immutabile / modificabile (usato per i pesi). |
| Esecuzione eager | Esecuzione immediata delle operazioni, come in Python (default in TensorFlow 2). |
| Grafo computazionale | Rappresentazione del calcolo con nodi (operazioni) e archi (tensori). |
| `tf.function` | Decoratore che trasforma una funzione Python in un grafo più veloce. |
| `tf.GradientTape` | Strumento che registra le operazioni e calcola automaticamente i gradienti. |
| `tf.data.Dataset` | Pipeline di input efficiente: `shuffle`, `map`, `batch`, `prefetch`. |
| GPU | Processore grafico, molto più veloce della CPU per i calcoli delle reti neurali. |

### 6.4 Keras
| Termine | Definizione |
|---|---|
| Keras | API di alto livello per costruire e addestrare reti neurali; Keras 3 supporta i backend TensorFlow, JAX e PyTorch. |
| Backend | Libreria che esegue effettivamente i calcoli sotto Keras. |
| Modello Sequenziale (`keras.Sequential`) | Modello con strati in sequenza lineare, un input e un output. |
| Modello Funzionale (`keras.Model`) | Modello costruito applicando gli strati ai tensori; ammette più input/output e rami. |
| `keras.Input` | Dichiarazione della forma dei dati in ingresso. |
| `Flatten` | Strato che appiattisce un input multidimensionale in un vettore. |
| `Concatenate` | Strato che affianca le uscite di più rami. |
| `compile` | Configura ottimizzatore, loss e metriche prima dell'addestramento. |
| `fit` / `evaluate` / `predict` | Addestramento / valutazione / previsione di un modello Keras. |
| History | Oggetto restituito da `fit` con loss e metriche per epoca (`history.history`). |
| `summary` / `count_params` | Tabella degli strati e dei parametri / numero totale di parametri. |
| `set_random_seed` | Fissa i semi casuali per risultati riproducibili. |

### 6.5 Reti dense per dati tabellari e immagini
| Termine | Definizione |
|---|---|
| Uscita lineare | Ultimo strato senza attivazione, usato per la regressione. |
| `sparse_categorical_crossentropy` | Loss multiclasse con etichette intere (0, 1, 2…). |
| `to_categorical` | Funzione Keras che converte le etichette intere in one-hot. |
| `argmax` | Indice del valore massimo: trasforma le probabilità softmax nella classe prevista. |
| Multi-etichetta | Problema in cui un campione può appartenere a più classi insieme. |
| Pixel | Singolo punto di un'immagine; in scala di grigi vale 0 (nero)–255 (bianco). |
| Canale | Componente di colore di un'immagine (1 in scala di grigi, 3 in RGB). |
| `validation_split` | Usa l'ultima frazione dei dati di training, senza mescolarla, come validazione. |
| `validation_data` | Validation set passato esplicitamente a `fit`. |

---

## Giorno 7 — Valutazione, regolarizzazione, reti convoluzionali

### 7.1 Valutare e diagnosticare una rete
| Termine | Definizione |
|---|---|
| Curve di addestramento | Grafici di loss e metriche per epoca su training e validazione (`history.history`). |
| `val_loss` / `val_accuracy` | Loss e accuratezza calcolate sui dati di validazione a ogni epoca. |
| Confidenza | Probabilità assegnata dal modello alla classe scelta (`np.max` delle probabilità). |
| Analisi degli errori | Esame dei campioni classificati male, soprattutto quelli con alta confidenza. |

### 7.2 Overfitting e regolarizzazione
| Termine | Definizione |
|---|---|
| Dropout | Strato che durante l'addestramento spegne a caso una frazione di neuroni; inattivo in predizione. |
| `kernel_regularizer` | Parametro di uno strato per aggiungere una penalità L1/L2 sui pesi. |
| Early stopping | Interruzione dell'addestramento quando la metrica di validazione smette di migliorare. |
| `patience` | Numero di epoche senza miglioramenti da attendere prima di fermarsi. |
| `restore_best_weights` | Ripristino dei pesi dell'epoca migliore alla fine dell'early stopping. |
| Callback | Oggetto chiamato da Keras durante `fit` (es. EarlyStopping, ModelCheckpoint, ReduceLROnPlateau). |
| `ModelCheckpoint` | Callback che salva su file il modello migliore durante l'addestramento. |
| BatchNormalization | Strato che normalizza le uscite di uno strato, stabilizzando e velocizzando l'addestramento. |

### 7.3 Reti neurali convoluzionali (CNN)
| Termine | Definizione |
|---|---|
| CNN (rete convoluzionale) | Rete neurale che usa convoluzioni per sfruttare la struttura spaziale delle immagini. |
| Convoluzione | Operazione in cui un filtro scorre sull'immagine calcolando somme pesate dei pixel sottostanti. |
| Filtro (kernel) | Piccola griglia di pesi imparati (es. 3×3) che rileva un motivo nell'immagine. |
| Feature map | Immagine prodotta da un filtro: indica dove compare il motivo rilevato. |
| Condivisione dei pesi | Uso dello stesso filtro in tutte le posizioni dell'immagine. |
| Stride (passo) | Numero di pixel di cui si sposta il filtro a ogni passo. |
| Padding (`valid` / `same`) | Nessun bordo, l'uscita si riduce / bordo di zeri, l'uscita mantiene la dimensione. |
| Pooling (`MaxPooling2D`) | Riduzione delle feature map tenendo il massimo di ogni blocco (es. 2×2). |
| `Conv2D` | Strato convoluzionale 2D di Keras; parametri: `(k·k·canali_in + 1) × filters`. |
| `GlobalAveragePooling2D` | Strato che riduce ogni feature map alla sua media; alternativa leggera a `Flatten`. |

### 7.4 Data augmentation, salvataggio e transfer learning
| Termine | Definizione |
|---|---|
| Data augmentation | Creazione di varianti realistiche delle immagini di training per ridurre l'overfitting. |
| `RandomFlip` / `RandomRotation` / `RandomZoom` / `RandomContrast` | Strati Keras di augmentation, attivi solo in addestramento. |
| `Rescaling` | Strato che normalizza i pixel dentro il modello. |
| Formato `.keras` | File che contiene architettura, pesi e stato dell'ottimizzatore (`model.save`, `load_model`). |
| Transfer learning | Riutilizzo di una rete pre-addestrata su un grande dataset per un nuovo problema. |
| ImageNet | Dataset di oltre un milione di immagini in 1000 categorie, usato per pre-addestrare le CNN. |
| `include_top=False` | Caricamento di un modello pre-addestrato senza lo strato finale di classificazione. |
| Congelare (`trainable = False`) | Bloccare i pesi di una parte della rete durante l'addestramento. |
| Fine-tuning | Riaddestramento di alcuni strati pre-addestrati con learning rate molto basso. |
| `image_dataset_from_directory` | Funzione che crea un dataset di immagini da cartelle, una per classe. |

### 7.5 scikit-learn o Keras?
| Termine | Definizione |
|---|---|
| Baseline | Modello semplice di riferimento da cui partire e da battere. |
| Cross-validation con Keras | Ciclo manuale con `StratifiedKFold` che crea un modello nuovo e ripete il preprocessing a ogni fold. |
