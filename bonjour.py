#!/usr/bin/env python3
"""
Mon premier script Python

par: Thomas Barkley
"""

import time


def main():
    """
    fonction principale du script
    """
    print("Bonjour python!")
    print("\nJe suis Thomas Barkley")
    compter_jusqua(10)


def compter_jusqua(limite_sup):
    """
    affiche progressivement une séquence de nombre à partir de 1 en montant
    
    :param limite_sup: jusqu'à ou compter
    """
    print(f"et je sais compter jusqu'à {limite_sup}: ", end="", flush=True)
    for i in range(1, 11):
        time.sleep(0.25)
        print(i, " ", end="", flush=True)
    print()


if __name__ == "__main__":
    main()
