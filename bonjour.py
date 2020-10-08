#!/usr/bin/env python3
# Mon premier script Python

import time

def main():
    print("Bonjour python!")
    print("\nJe suis Thomas Barkley")
    n = 10
    print(f"et je sais compter jusqu'à {n}: ",end="",flush=True)
    for i in range(1,11):
        time.sleep(0.25)
        print(i, " ", end="",flush=True)
    print()


if __name__ == "__main__":
    main()