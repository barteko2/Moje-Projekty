#!/usr/bin/env python
"""proste narzędzie wierza polecenia korzystające z atrybutu sys.argv"""

import sys

def say_it(greeting,target):
    message = f'{greeting} {target}'
    print(message)

if __name__ == '__main__':
    greeting = 'Witaj'
    name = 'Bartek'

    if '--help' in sys.argv:
        help_message = f"Sposób użycia: {sys.argv[0]} --name<IMIE> --greeting <POWITANIE>"
        print(help_message)

    if '--name' in sys.argv:
        name_index = sys.argv.index('--name') + 1

        if name_index < len(sys.argv):
            name = sys.argv[name_index]

        if '--greeting' in sys.argv:
            greeting_index = sys.argv.index('--greeting') + 1

        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

say_it(greeting, name)