#!/usr/bin/env python

import fire
import pkgutil
import importlib

def find_and_run_plugins(plugin_prefix):
    plugins = {}

    #Wykrywanie i ładowanie wtyczek
    print(f"wtyczek z prefiksem: {plugin_prefix}")
    for _, name, _ in pkgutil.iter_modules():
        if name.startswith(plugin_prefix):
            module = importlib.import_module(name)
            plugins[name] = module

    #uruchamianie wtyczek
    for name, module in plugins.items():
        print(f"uruchomienie wtyczki {name}")
        module.run()

if __name__ == '__main__':
    fire.Fire()