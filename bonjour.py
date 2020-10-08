#!/usr/bin/env python3
# Mon premier script Python

import time

def main():
    print("Bonjour python!")
    print("\nJe suis Thomas Barkley")
    print("et je sais compter jusqu'à 10: ",end="",flush=True)
    for i in range(1,11):
        time.sleep(0.25)
        print(i, " ", end="",flush=True)
    print()


if __name__ == "__main__":
    main()