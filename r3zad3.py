#!/usr/bin/env python3
"""skorzystaj z pakietu fire w celu uzyskania
(z wiersza polecenia) dostępu do metod z istniejącego
skryptu pythona"""
import podparsery
import fire
class przyklady():
    def podparser(self):
        podparsery.sail()
    def podparser1(self):
        podparsery.list_ships()
class Cli():
    def __init__(self):
        self.przyklady = przyklady()

if __name__ == '__main__':
    fire.Fire(Cli)