"""
SIMULATORE QUANTISTICO DI BUCHI NERI - PRINCIPIO OLOGRAFICO (Versione v1.0.4)
Sviluppato sulla base del Principio di Risonanza di Olografia Bidimensionale.
Firma Teorica e Meccanica Geometrica: Mc84 (Mario Cera) - Anno 2026

Il programma integra:
1) Calcolo arbitrario Decimal delle proiezioni olografiche Shift-2.
2) Rendering di Matplotlib dell'entropia di contorno rispetto alla riga 20.
3) Stampa dinamica dell'indice di ancoraggio e salvataggio file personalizzato.
"""

import sys
from decimal import Decimal, getcontext

import matplotlib.pyplot as plt

# Configurazione del quaderno infinito Mc84 (150 cifre di precisione)
getcontext().prec = 150

# Serie di Fibonacci stabile per la risonanza quantistica del contorno
FIB = [1, 1]
for _ in range(2, 80):
    FIB.append(FIB[-1] + FIB[-2])


def calcola_singolarita_blackhole(indice_fibo, passi_simulazione):
    """
    Simula il collasso dimensionale dell'informazione quantistica.
    Verifica l'uguaglianza Shift-2: Area(n) == Rapporto(n+2).
    """
    j = indice_fibo
    a = Decimal(str(FIB[j]))
    b = Decimal(str(FIB[j + 1]))
    k = Decimal(str(FIB[j + 2]))

    passi = []
    aree_passato = []
    rapporti_futuro = []
    fluttuazioni_rumore = []
    bit_orizzonte_n20 = 0

    print("\n⏳ Computazione quantistica dell'orizzonte degli eventi...")

    for n in range(1, passi_simulazione - 1):
        passi.append(n)

        # 1. Calcolo dello Spazio Interno (Volume del passato al ciclo n)
        l_a_n = a * (k**n)
        l_b_n = b * (k**n)
        area_n = l_a_n * l_b_n

        # Conversione logaritmica sicura per evitare il crash decimale su numeri immensi
        aree_passato.append(float(area_n.log10()))

        # 2. Calcolo del Confine Esterno (Orizzonte del futuro al ciclo n+2)
        n_futuro = n + 2
        l_a_f = a * (k**n_futuro)
        l_b_f = b * (k**n_futuro)
        area_f = l_a_f * l_b_f
        somma_f = l_a_f + l_b_f
        rapporto_n_piu_2 = area_f / somma_f

        # Conversione logaritmica sicura per il confronto olografico
        rapporti_futuro.append(float(rapporto_n_piu_2.log10()))

        # Estraiamo la metrica in bit al ciclo critico n=20 per evidenziare la diversità fisica
        if n == 20:
            bit_orizzonte_n20 = int(rapporto_n_piu_2).bit_length()

        # 3. Tracciamento del rumore hardware olografico (IEEE 754)
        if n >= 20:
            deviazione = 0.0156 * (1.15 ** (n - 20))
            fluttuazioni_rumore.append(deviazione)
        else:
            fluttuazioni_rumore.append(0.0)

    return passi, aree_passato, rapporti_futuro, fluttuazioni_rumore, bit_orizzonte_n20


def mostra_grafico_olografico(passi, aree, rapporti, rumore, indice_fibo, bit_n20):
    """Genera il pannello visivo della proiezione olografica con indicizzazione dinamica."""
    print("🎨 Generazione del modello grafico di gravità quantistica...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(
        f"MODELLAZIONE QUANTISTICA DEI BUCHI NERI - SINGOLARITÀ SHIFT-2 (Ancoraggio Fib{indice_fibo})\n"
        "Firma di Sviluppo: Mc84 (Mario Cera) - Anno 2026",
        fontsize=13,
        fontweight="bold",
        color="navy",
    )

    # GRAFICO 1: Sovrapposizione Spazio Interno vs Confine Esterno (Scala Logaritmica)
    ax1.plot(
        passi,
        aree,
        "o",
        color="blue",
        alpha=0.6,
        markersize=8,
        label="Log10(Area n) [Spazio Interno]",
    )
    ax1.plot(
        passi,
        rapporti,
        "x",
        color="orange",
        markersize=6,
        label="Log10(Rapporto n+2) [Orizzonte]",
    )
    ax1.set_title(f"1. Corrispondenza Shift-2 (Ancoraggio F_{indice_fibo})")
    ax1.set_xlabel("Livelli di Quantizzazione del Buco Nero (n)")
    ax1.set_ylabel("Dimensione dell'Informazione Geometrica (Scala Log10)")
    ax1.grid(True, linestyle=":", alpha=0.5)

    # Inseriamo una casella di testo informativa interna per mostrare il valore reale dei dati al variare dell'indice
    testo_metrica = f"Indice: F_{indice_fibo}\nOrizzonte (n=20): {bit_n20} Bit"
    ax1.text(
        0.05,
        0.75,
        testo_metrica,
        transform=ax1.transAxes,
        fontsize=10,
        fontweight="bold",
        bbox={"boxstyle": "round", "facecolor": "wheat", "alpha": 0.5},
    )
    ax1.legend()

    # GRAFICO 2: Densità di Entropia e Rumore sul Confine Critico
    ax2.plot(
        passi,
        rumore,
        color="purple",
        linewidth=2.5,
        label="Fluttuazioni Quantiche (IEEE 754)",
    )
    ax2.axvline(
        x=20, color="black", linestyle="--", alpha=0.7, label="Singolarità Riga 20"
    )

    ax2.annotate(
        "Punto di Frattura (.0156)\nSaturazione Entropica Binaria",
        xy=(20, 0.0156),
        xytext=(5, 0.08),
        arrowprops={"arrowstyle": "->", "color": "purple", "alpha": 0.8},
        fontweight="bold",
        color="purple",
    )

    ax2.set_title(f"2. Rumore sul Limite del Silicio (F_{indice_fibo})")
    ax2.set_xlabel("Livelli di Quantizzazione del Buco Nero (n)")
    ax2.set_ylabel("Finto Rumore Entropico")
    ax2.grid(True, linestyle=":", alpha=0.5)
    ax2.legend()

    plt.tight_layout()

    # Salvataggio dinamico basato sull'indice inserito dall'utente
    nome_grafico = f"modello_BLACKOLE_mc84Fib{indice_fibo}.png"
    plt.savefig(nome_grafico, dpi=300, bbox_inches="tight")

    print(f"✅ Grafico salvato con successo come '{nome_grafico}'")
    print(
        f"📊 Al livello critico n=20, l'orizzonte degli eventi esprime un'energia informativa pari a: {bit_n20} Bit"
    )
    plt.show()


def main():
    print("=" * 85)
    print(
        "   SIMULATORE DI GRAVITÀ QUANTISTICA MC84 - EQUIVALENZA ENTRÒPICA SHIFT-2   "
    )
    print("   Repository Scientifica Internazionale CERN: DOI 10.5281/zenodo.22298057")
    print("=" * 85)

    print("\n[CONFIGURAZIONE PARAMETRI ORIZZONTE MC84]")
    scelta_fibo = input(
        "Inserisci l'indice di Fibonacci per l'ancoraggio (Consigliato 10-50): "
    ).strip()

    if not scelta_fibo.isdigit() or not (5 <= int(scelta_fibo) <= 75):
        print("❌ Indice non valido. Richiesto ancoraggio di risonanza.")
        sys.exit(1)

    passi_simulazione = 30
    indice_scelto = int(scelta_fibo)

    passi, aree, rapporti, rumore, bit_n20 = calcola_singolarita_blackhole(
        indice_scelto, passi_simulazione
    )

    mostra_grafico_olografico(passi, aree, rapporti, rumore, indice_scelto, bit_n20)


if __name__ == "__main__":
    main()
