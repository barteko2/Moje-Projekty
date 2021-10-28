#!/usr/bin/env python3
"""Wykorzystaj moduł sys do napisania skryptu
który wyświetla wiersz tylko wtedy gdy skrypt
został uruchomiony z wiersza polecenia"""
import sys
#!!!!!!!!!!!!!!!!sysargv
if __name__ == '__main__':
    print(f"Pierwszy argument: {sys.argv[0]}")
    if sys.argv[0] == "./r3zad1.py":
        print("wyświetlam wiersz")

