#!/usr/bin/env python3
"""Skorzystaj z modułu click, aby stworzyć narzędzie
wiersza polecenia, które przyjmuje nazwę jako argument
i wyświetla ją, jeśli nie rozpoczyna się na 'p'."""
import click


@click.command()
@click.option('--name', default='Pupa', help='Podaj argument')
def sprawdz_czyP(name):
    check = str(name)
    if (check.startswith("p")) == True:
        print("dupa")
    else:
        print(name)



if __name__ == '__main__':
    sprawdz_czyP()