#!/usr/bin/env python
"""proste narzędzie wierza polecenia korzystające z atrybutu sys.argv"""
"""MEGA ZAJEBISTY PATENT!!!!!!"""
import argparse

def sail():
    ship_name = 'Twoja żaglówka'
    print(f"{ship_name} stawia żagle")

def list_ships():
    ships = ['John B', 'Yankee Clipper','Pequod']
    print(f"Żaglówki:{','.join(ships)}")

def greet(greeting, name):
    message = f'{greeting}{name}'
    print(message)

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Żeglarze i Żaglówki')

    parser.add_argument('--twice','-t', help = "zrób to dwukrotnie", action = 'store_true')
    subparsers = parser.add_subparsers(dest = 'func')
    ship_parser = subparsers.add_parser('ships',help = 'Komendy związane z żaglówkami')

    ship_parser.add_argument('command', choices=['list', 'sail'])

    sailor_parser = subparsers.add_parser('sailors', help = "komendy zwiazane z zeglarzami")

    sailor_parser.add_argument('name', help = 'Imię żeglarza')

    sailor_parser.add_argument('--greeting','-g',help='pozdrowienie',default='Ahoj żeglarzu')

    args = parser.parse_args()
    if args.func == 'sailors':
        greet(args.greeting,args.name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()