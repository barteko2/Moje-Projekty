import click

from numba import(cuda,vectorize)
import numba
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

def timing(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        ts = time()
        result = f(*args,**kwargs)
        te = time()
        print(f"fun: {f.__name__}, argumenty: [{args},{kwargs}] zajęło: {te-ts} sek")
        return result
    return wrap