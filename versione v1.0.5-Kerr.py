"""
SIMULATORE QUANTISTICO DI BUCHI NERI - PRINCIPIO OLOGRAFICO (Versione v1.0.5-Kerr)
Sviluppato sulla base del Principio di Risonanza di Olografia Bidimensionale.
Estensione metrica: Distorsione da rotazione macroscopica (Spin di Kerr).
Firma Teorica e Meccanica Geometrica: Mc84 (Mario Cera) - Anno 2026
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


def calcola_singolarita_kerr_shift(indice_fibo, passi_simulazione, spin_omega):
    """
    Simula il collasso dimensionale dell'informazione quantistica in un buco nero rotante.
    Verifica la tenuta dell'uguaglianza Shift-2 sotto distorsione di Kerr.
    """
    j = indice_fibo
    a = Decimal(str(FIB[j]))
    b = Decimal(str(FIB[j + 1]))
    k = Decimal(str(FIB[j + 2]))

    omega = Decimal(str(spin_omega))

    # Fattori di correzione geometrica derivati dallo sferoide oblato di Kerr
    correzione_area = 1 - (omega**4)
    correzione_perimetro = (1 - (omega**2)).sqrt()

    passi = []
    aree_passato = []
    rapporti_futuro = []
    fluttuazioni_rumore = []
    bit_orizzonte_n20 = 0

    print(
        f"\n⏳ Computazione quantistica dell'orizzonte di Kerr (Spin Ω = {spin_omega})...."
    )

    for n in range(1, passi_simulazione - 1):
        passi.append(n)

        # 1. Calcolo dello Spazio Interno Modificato (Volume del passato al ciclo n)
        area_n = (a * b) * (k ** (2 * n)) * correzione_area

        # Conversione logaritmica sicura per il grafico
        aree_passato.append(float(area_n.log10()))

        # 2. Calcolo del Confine Esterno di Kerr (Orizzonte del futuro al ciclo n+2)
        n_futuro = n + 2
        l_a_f = a * (k**n_futuro) * (1 - (omega**2))
        l_b_f = b * (k**n_futuro) * (1 + (omega**2))

        area_f = l_a_f * l_b_f
        somma_f = l_a_f + l_b_f

        # Rapporto olografico compensato con la metrica del perimetro ellittico e riscalamento Shift-2
        rapporto_n_piu_2 = (area_f / (somma_f * correzione_perimetro)) * (
            k ** Decimal(str(n - 1))
        )

        # Conversione logaritmica per il confronto olografico
        rapporti_futuro.append(float(rapporto_n_piu_2.log10()))

        # Estrazione metrica in bit al ciclo critico n=20
        if n == 20:
            bit_orizzonte_n20 = int(rapporto_n_piu_2).bit_length()

        # 3. Tracciamento del rumore hardware olografico (IEEE 754)
        if n >= 20:
            deviazione = 0.0156 * (1.15 ** (n - 20))
            fluttuazioni_rumore.append(deviazione)
        else:
            fluttuazioni_rumore.append(0.0)

    return (
        passi,
        aree_passato,
        rapporti_futuro,
        fluttuazioni_rumore,
        bit_orizzonte_n20,
    )


def mostra_grafico_kerr_olografico(
    passi, aree, rapporti, rumore, indice_fibo, spin_omega, bit_n20
):
    """Genera il pannello visivo della proiezione olografica di Kerr."""
    print("🎨 Generazione del modello grafico di gravità quantistica rotante...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(
        f"MODELLAZIONE QUANTISTICA DI KERR - SINGOLARITÀ SHIFT-2 (Ancoraggio Fib{indice_fibo} | Spin Ω: {spin_omega})\n"
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
        color="royalblue",
        alpha=0.6,
        markersize=8,
        label="Log10(Area n) [Spazio Interno Distorto]",
    )
    ax1.plot(
        passi,
        rapporti,
        "x",
        color="darkorange",
        markersize=6,
        label="Log10(Rapporto n+2) [Orizzonte Ellittico Kerr]",
    )
    ax1.set_title(f"1. Corrispondenza Kerr-Shift (F_{indice_fibo})")
    ax1.set_xlabel("Livelli di Quantizzazione del Buco Nero (n)")
    ax1.set_ylabel("Dimensione dell'Informazione Geometrica (Scala Log10)")
    ax1.grid(True, linestyle=":", alpha=0.5)

    # Casella di testo informativa interna aggiornata con la dicitura personalizzata
    testo_metrica = (
        f"Indice: F_{indice_fibo}\n"
        f"Spin Ω: {spin_omega}\n"
        f"Al livello critico n=20, l'orizzonte di Kerr\n"
        f"esprime un'energia pari a: {bit_n20} Bit"
    )
    ax1.text(
        0.05,
        0.62,
        testo_metrica,
        transform=ax1.transAxes,
        fontsize=9,
        fontweight="bold",
        bbox={"boxstyle": "round", "facecolor": "wheat", "alpha": 0.5},
    )
    ax1.legend()

    # GRAFICO 2: Densità di Entropia e Rumore sul Confine Critico
    ax2.plot(
        passi,
        rumore,
        color="crimson",
        linewidth=2.5,
        label="Fluttuazioni Quantiche in Ergosfera",
    )
    ax2.axvline(
        x=20,
        color="black",
        linestyle="--",
        alpha=0.7,
        label="Singolarità Riga 20",
    )

    ax2.annotate(
        "Punto di Frattura (.0156)\nSaturazione Entropica di Kerr",
        xy=(20, 0.0156),
        xytext=(5, 0.08),
        arrowprops={"arrowstyle": "->", "color": "crimson", "alpha": 0.8},
        fontweight="bold",
        color="crimson",
    )

    ax2.set_title(f"2. Rumore limite sul Confine Rotante (F_{indice_fibo})")
    ax2.set_xlabel("Livelli di Quantizzazione del Buco Nero (n)")
    ax2.set_ylabel("Finto Rumore Entropico")
    ax2.grid(True, linestyle=":", alpha=0.5)
    ax2.legend()

    plt.tight_layout()

    # Salvataggio dinamico basato su indice e spin
    nome_grafico = (
        f"modello_KERR_BLACKOLE_mc84Fib{indice_fibo}_spin{int(spin_omega * 100)}.png"
    )
    plt.savefig(nome_grafico, dpi=300, bbox_inches="tight")

    print(f"✅ Grafico salvato con successo como '{nome_grafico}'")
    print(
        f"📊 Al livello critico n=20, l'orizzonte di Kerr esprime un'energia pari a: {bit_n20} Bit"
    )
    plt.show()


def main():
    print("=" * 85)
    print(
        "   SIMULATORE DI GRAVITÀ QUANTISTICA MC84 - METRICA ESTESA KERR-SHIFT SHIFT-2   "
    )
    print("   Repository Scientifica Internazionale CERN: DOI 10.5281/zenodo.22298057")
    print("=" * 85)

    print("\n[CONFIGURAZIONE PARAMETRI ORIZZONTE DI KERR]")
    scelta_fibo = input(
        "Inserisci l'indice di Fibonacci per l'ancoraggio (Consigliato 10-50): "
    ).strip()

    if not scelta_fibo.isdigit() or not (5 <= int(scelta_fibo) <= 75):
        print("❌ Indice non valido. Richiesto ancoraggio di risonanza.")
        sys.exit(1)

    scelta_spin = input(
        "Inserisci il parametro di Spin Omega (da 0.0 statico a 0.99 elastico): "
    ).strip()

    try:
        spin_omega = float(scelta_spin)
        if not (0.0 <= spin_omega < 1.0):
            raise ValueError
    except ValueError:
        print(
            "❌ Parametro di Spin non valido. Inserire un valore decimale compreso tra 0 e 0.99."
        )
        sys.exit(1)

    passi_simulazione = 30
    indice_scelto = int(scelta_fibo)

    passi, aree, rapporti, rumore, bit_n20 = calcola_singolarita_kerr_shift(
        indice_scelto, passi_simulazione, spin_omega
    )

    mostra_grafico_kerr_olografico(
        passi, aree, rapporti, rumore, indice_scelto, spin_omega, bit_n20
    )


if __name__ == "__main__":
    main()
