#!/usr/bin/env python
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wyświetla wprowadzone dane wejściowe')
    parser.add_argument('komunikat',help='Komunikat do wyświetlenia')
    parser.add_argument('--twice','-t', help='Zrób to dwukrotnie',action='store_true')

    args = parser.parse_args()

    print(args.komunikat)
    if args.twice:
        print(args.komunikat)
