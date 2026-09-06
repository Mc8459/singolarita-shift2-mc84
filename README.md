# 🌀 Analisi Multiscala della Singolarità Shift-2 e del Principio Olografico Mc84

Repository scientifico ufficiale dedicato alla validazione computazionale del **Principio di Risonanza di Olografia Bidimensionale**, applicato alla fisica teorica dei buchi neri e alla gestione dell'entropia di contorno. 

Il modello estende i principi geometrici discussi nel *Modulo Prototipale di Validazione Bit (v1.0.3)* ed è collegato alle pubblicazioni depositate sul server del CERN via Zenodo.

---

## 🔬 Contesto Teorico: L'Algoritmo Mc84

Nella fisica contemporanea, il **Paradosso dell'Informazione di Hawking** evidenzia il contrasto tra la Relatività Generale (l'informazione che attraversa l'orizzonte degli eventi viene persa) e la Meccanica Quantistica (l'informazione deve conservarsi, principio di unitarietà).

L'algoritmo **Mc84 (Sviluppato da Mario Cera - 2026)** offre una soluzione computazionale pura e autonoma attraverso la **Singolarità Shift-2**:
* **Equivalenza Geometrica:** Tutta l'informazione contenuta all'interno di un volume di spazio quadratico ($Area_n$) viene proiettata e si manifesta intatta come valore della proiezione lineare sul perimetro bidimensionale due iterazioni temporali più tardi ($Rapporto_{n+2}$).
* **Risonanza di Fibonacci:** L'utilizzo di triadi consecutive di Fibonacci $[F_j, F_{j+1}, F_{j+2}]$ neutralizza l'impianto frazionario dei denominatori ($a + b = k$), azzerando il rumore quantistico sul confine e garantendo un'archiviazione a entropia controllata fino alla riga di collasso hardware del silicio (Fissata al livello critico $n = 20$).

---

## 📦 Contenuto del Repository

I file all'interno del repository sono organizzati in ordine alfabetico per una consultazione immediata:

1. 📄 **`1_Analisi_Multiscala_Shift2.pdf`**: Documentazione teorica completa contenente l'interpretazione dei grafici (Fib5, Fib27, Fib50), le dinamiche olografiche di compressione spaziale e la formalizzazione algebrica del collasso dimensionale.
2. 🐍 **`2_simulatore_buchi_neri.py`**: Script interattivo in Python (v1.0.4) che esegue la simulazione numerica ad alta precisione (150 cifre decimali) e genera i relativi pannelli visivi tramite Matplotlib.

---

## 🛠️ Come Utilizzare il Simulatore Python

Il programma richiede l'installazione della libreria grafica `matplotlib`.

### Pre-requisiti
Assicurati di avere installato le dipendenze necessarie eseguendo nel terminale:
```bash
pip install matplotlib
```

### Esecuzione
Avvia lo script con il comando:
```bash
python 2_simulatore_buchi_neri.py
```
Il simulatore ti chiederà di inserire un **indice di ancoraggio di Fibonacci** (valore consigliato tra `10` e `50`). Al termine dell'elaborazione, il programma:
* Mostrerà la perfetta invarianza di forma logaritmica (andamento rettilineo e parallelo tra Spazio Interno e Orizzonte).
* Evidenzierà il punto di frattura analitico (`.0156`) indotto dallo standard di approssimazione IEEE 754 oltre il livello $n=20$.
* Salverà automaticamente un grafico ad alta risoluzione in formato `.png` specifico per l'indice scelto (es. `modello_BLACKOLE_mc84Fib10.png`).

---

## 📐 Riferimenti e Contatti

* **Autore ed Enunciatore Teorico:** Mc84 (Mario Cera)
* **Laboratorio:** Laboratorio Computazionale di Olografia Geometrica (Roma, San Cesareo - Italia)
* **Repository Principale di Riferimento:** Codice su ZENODO (DOI: 10.5281/zenodo.22298057)
* **E-mail Ufficiale:** mario.cera@hotmail.it
* **Licenza:** Creative Commons Attribution 4.0 International (CC-BY-4.0)
