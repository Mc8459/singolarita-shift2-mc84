"""
SIMULATORE QUANTISTICO DI BUCHI NERI - PRINCIPIO OLOGRAFICO (Versione v1.3.0-Universal)
Sviluppato sulla base del Principio di Risonanza di Olografia Bidimensionale.
Integrazione Metrica Totale: Massa, Spin Dinamico e Carica Elettrica Netta.
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


def calcola_singolarita_universale_shift(
    indice_fibo, passi_simulazione, spin_omega, carica_q
):
    """
    Simula il collasso dell'informazione quantistica accoppiando massa, spin e carica.
    Valida la tenuta dell'invarianza formale Shift-2 sotto l'azione combinata dei campi.
    """
    j = indice_fibo
    a = Decimal(str(FIB[j]))
    b = Decimal(str(FIB[j + 1]))
    k = Decimal(str(FIB[j + 2]))

    omega = Decimal(str(spin_omega))
    q = Decimal(str(carica_q))

    # Fattori di correzione geometrica di Kerr-Newman (Sferoide oblato + compressione isotropa)
    correzione_area = (1 - (omega**4)) * (1 - (q**2))
    correzione_perimetro = ((1 - (omega**2)) * (1 - (q**2))).sqrt()

    passi = []
    aree_passato = []
    rapporti_futuro = []
    fluttuazioni_rumore = []
    bit_orizzonte_n20 = 0

    print(
        f"\n⏳ Computazione quantistica universale (Spin Ω = {spin_omega} | Carica Q = {carica_q})..."
    )

    for n in range(1, passi_simulazione - 1):
        passi.append(n)

        # 1. Calcolo dello Spazio Interno Modificato
        area_n = (a * b) * (k ** (2 * n)) * correzione_area
        aree_passato.append(float(area_n.log10()))

        # 2. Calcolo del Confine Esterno Olografico (Ciclo n+2)
        n_futuro = n + 2
        l_a_f = a * (k**n_futuro) * (1 - (omega**2)) * (1 - (q**2)).sqrt()
        l_b_f = b * (k**n_futuro) * (1 + (omega**2)) * (1 - (q**2)).sqrt()

        area_f = l_a_f * l_b_f
        somma_f = l_a_f + l_b_f

        # Rapporto olografico compensato con i modificatori geometrici e riscalamento Shift-2
        modificatore_singolarita = somma_f * correzione_perimetro
        rapporto_n_piu_2 = (area_f / modificatore_singolarita) * (
            k ** Decimal(str(n - 1))
        )
        rapporti_futuro.append(float(rapporto_n_piu_2.log10()))

        # Estrazione quantica dell'orizzonte a n=20
        if n == 20:
            bit_orizzonte_n20 = int(rapporto_n_piu_2).bit_length()

        # 3. TRACCIAMENTO RUMORE CON DOPPIO ACCOPPIAMENTO DI GAUGE (Spin + Carica)
        if n >= 20:
            gamma_0 = Decimal("0.15")
            # Lo scudo quantistico risente del bilanciamento di entrambe le forze repulsive
            fattore_gauge = ((1 - (omega**2)) * (1 - (q**2))).sqrt()
            base_rumore = 1 + (gamma_0 * fattore_gauge)

            deviazione = Decimal("0.0156") * (base_rumore ** (n - 20))
            fluttuazioni_rumore.append(float(deviazione))
        else:
            fluttuazioni_rumore.append(0.0)

    return passi, aree_passato, rapporti_futuro, fluttuazioni_rumore, bit_orizzonte_n20


def mostra_grafico_universale_olografico(
    passi, aree, rapporti, rumore, indice_fibo, spin_omega, carica_q, bit_n20
):
    """Genera il pannello visivo della proiezione olografica universale Mc84."""
    print("🎨 Generazione del modello grafico di gravità quantistica universale...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5))

    fig.suptitle(
        "MODELLAZIONE QUANTISTICA UNIVERSALE - SINGOLARITÀ SHIFT-2 (v1.3.0)\n"
        "Firma di Sviluppo: Mc84 (Mario Cera) - Anno 2026",
        fontsize=13,
        fontweight="bold",
        color="navy",
        y=0.98,
    )

    # GRAFICO 1: Sovrapposizione Olografica
    ax1.plot(
        passi,
        aree,
        "o",
        color="royalblue",
        alpha=0.6,
        markersize=8,
        label="Log10(Area n) [Spazio Interno]",
    )
    ax1.plot(
        passi,
        rapporti,
        "x",
        color="darkorange",
        markersize=6,
        label="Log10(Rapporto n+2) [Confine Orizzonte]",
    )
    ax1.axvline(
        x=20, color="black", linestyle="--", alpha=0.5, label="Singolarità Riga 20"
    )

    ax1.set_title(
        f"1. Corrispondenza Geometrica (Ancoraggio F_{indice_fibo})",
        pad=20,
        fontweight="bold",
    )
    ax1.set_xlabel("Livelli di Quantizzazione del Buco Nero (n)", labelpad=10)
    ax1.set_ylabel("Dimensione dell'Informazione Geometrica (Scala Log10)", labelpad=10)
    ax1.grid(True, linestyle=":", alpha=0.5)
    ax1.legend(loc="upper left", frameon=True, shadow=True)

    # Box informativo in puro testo per azzerare i warning sui font del terminale
    testo_metrica = (
        "METRICHE DI SINTESI\n"
        f"  Indice: F_{indice_fibo}\n"
        f"  Spin Omega: {spin_omega}\n"
        f"  Carica Q: {carica_q}\n"
        f"  Energia a n=20: {bit_n20} Bit"
    )
    ax1.text(
        0.52,
        0.05,
        testo_metrica,
        transform=ax1.transAxes,
        fontsize=9,
        fontweight="bold",
        bbox={
            "boxstyle": "round,pad=0.6",
            "facecolor": "wheat",
            "alpha": 0.7,
            "edgecolor": "orange",
        },
    )

    # GRAFICO 2: Densità di Rumore e Scudo Quantistico
    ax2.plot(
        passi,
        rumore,
        color="crimson",
        linewidth=2.5,
        label="Fluttuazioni Quantiche (Gauge Combinato)",
    )
    ax2.axvline(
        x=20, color="black", linestyle="--", alpha=0.7, label="Singolarità Riga 20"
    )

    ax2.annotate(
        "Punto di Frattura (.0156)\nSaturazione Dinamica",
        xy=(20, 0.0156),
        xytext=(2, 0.025),
        arrowprops={"arrowstyle": "->", "color": "crimson", "alpha": 0.8},
        fontweight="bold",
        color="crimson",
    )

    ax2.set_title(
        f"2. Rumore di Gauge sul Confine Universale (F_{indice_fibo})",
        pad=20,
        fontweight="bold",
    )
    ax2.set_xlabel("Livelli di Quantizzazione del Buco Nero (n)", labelpad=10)
    ax2.set_ylabel("Finto Rumore Entropico", labelpad=10)
    ax2.grid(True, linestyle=":", alpha=0.5)
    ax2.legend(loc="upper left", frameon=True, shadow=True)

    plt.tight_layout(rect=[0, 0, 1, 0.93])

    nome_grafico = f"modello_UNIVERSALE_mc84Fib{indice_fibo}_spin{int(spin_omega * 100)}_q{int(carica_q * 100)}.png"
    plt.savefig(nome_grafico, dpi=300, bbox_inches="tight")
    print(f"✅ Grafico salvato con successo come '{nome_grafico}'")
    plt.show()


def main():
    print("=" * 85)
    print(
        "   SIMULATORE DI GRAVITÀ QUANTISTICA UNIVERSALE MC84 - COMPILAZIONE DEFINITIVA  "
    )
    print("   Repository Scientifica Internazionale CERN: DOI 10.5281/zenodo.22298057")
    print("=" * 85)

    print("\n[CONFIGURAZIONE PARAMETRI STRUTTURALI]")
    scelta_fibo = input(
        "Inserisci l'indice di Fibonacci per l'ancoraggio (Consigliato 10-50): "
    ).strip()

    if not scelta_fibo.isdigit() or not (5 <= int(scelta_fibo) <= 75):
        print("❌ Indice non valido. Richiesto ancoraggio di risonanza.")
        sys.exit(1)

    scelta_spin = input(
        "Inserisci il parametro di Spin Omega (da 0.0 a 0.99) [0 per disattivare]: "
    ).strip()
    scelta_carica = input(
        "Inserisci il parametro di Carica Q (da 0.0 a 0.99) [0 per disattivare]: "
    ).strip()

    try:
        spin_omega = float(scelta_spin)
        carica_q = float(scelta_carica)
        if not (0.0 <= spin_omega < 1.0) or not (0.0 <= carica_q < 1.0):
            raise ValueError
    except ValueError:
        print(
            "❌ Parametri cinematici non validi. Inserire valori decimali compresi tra 0 e 0.99."
        )
        sys.exit(1)

    passi_simulazione = 30
    indice_scelto = int(scelta_fibo)

    passi, aree, rapporti, rumore, bit_n20 = calcola_singolarita_universale_shift(
        indice_scelto, passi_simulazione, spin_omega, carica_q
    )

    mostra_grafico_universale_olografico(
        passi, aree, rapporti, rumore, indice_scelto, spin_omega, carica_q, bit_n20
    )


if __name__ == "__main__":
    main()
