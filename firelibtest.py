#!/usr/bin/env python
"""
narzędzie korzystające z pakietu fire
"""

import fire

class Ships():
    def sail(self):
        ship_name='Twoja żaglówka'
        print(f"{ship_name} stawia żagle")

    def list(self):
        ships = ['Jan B', 'Stary Clipper','Strzała']
        print(f"Żaglówki: {','.join(ships)}")

def sailors(greeting,name):
    message = f'{greeting} {name}'
    print(message)

class Cli():
    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()

if __name__ == '__main__':
    fire.Fire(Cli)
