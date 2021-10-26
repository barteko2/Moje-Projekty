#!/usr/bin/env python
"""przykład użycia pakietu click"""
import click
"""
@click.command()
@click.option('--greeting',default = 'hej', help ='Jak chcesz pozdrowić użytkownika?')
@click.option('--name',default='Tomek',help = 'Kogo chcesz pozdrowić?')
def greet(greeting,name):
    print(f"{greeting} {name}")

if __name__ =='__main__':
    greet()
"""

@click.group()
def cli():
    pass

@click.group(help='Komendy związane z żaglówkami')
def ships():
    pass
cli.add_command(ships)

@ships.command(help='Żeglowanie Żaglówką')
def sail():
    ship_name = 'Twoja Żaglówka'
    print(f"{ship_name} stawia żagle")

@ships.command(help='Lista wszystkich żaglówek')
def list_ships():
    ships=['Jan B','Stary Clipper','Strzała']
    print(f"Żaglówki: {','.join(ships)}")

@cli.command(help='Komendy związane z żeglarzami')
@click.option('--greeting', default='Ahoj!!!', help='Pozdrowienie żeglarza')
@click.argument('name')
def sailors(greeting,name):
    message = f'{greeting} {name}'
    print(message)

if __name__ =='__main__':
    cli()