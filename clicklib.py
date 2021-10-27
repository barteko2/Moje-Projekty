#!/usr/bin/env python
"""przykład użycia pakietu click"""
import click
@click.command()
@click.option('--greeting',default = 'hej', help ='Jak chcesz pozdrowić użytkownika?')
@click.option('--name',default='Tomek',help = 'Kogo chcesz pozdrowić?')
def greet(greeting,name):
    print(f"{greeting} {name}")

if __name__ =='__main__':
    greet()



