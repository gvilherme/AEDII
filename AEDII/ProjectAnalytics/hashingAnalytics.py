import numpy as np
import pandas as pd
import math
from os import path
import matplotlib
import matplotlib.pyplot as plt
from AEDII.hashFunctions import hashFunctionByMod
from AEDII.hashFunctions import hashFunctionByMult

HERE = path.abspath(path.dirname(__file__))

def analysingModHash():
    m = 12
    r = 100
    print(f"Demonstração da função de espalhamento pelo método da divisão. M = {m}")
    df = resultsModHash(m, r)
    #save_df(df['Hashing results'], f"{m}_{r}_teste")
    histo = df['Hashing results'].value_counts()
    #df = pd.DataFrame({'hash_result':histo.index, 'count':histo.values})
    print(histo)
    save_df(df['Hashing results'], f"{m}_{r}")
    save_df(df, f"{m}_{r}_W_index")
    
    print("\n===========================================================\n")

    m = 11
    r = 100
    print(f"Demonstração da função de espalhamento pelo método da divisão. M = {m}")
    df = resultsModHash(m, r)
    histo = df['Hashing results'].value_counts()
    #df = pd.DataFrame({'hash_result':histo.index, 'count':histo.values})
    print(histo)
    save_df(df['Hashing results'], f"{m}_{r}")
    save_df(df, f"{m}_{r}_W_index")

    print("\n===========================================================\n")

    m = 97
    r = 10000
    print(f"Demonstração da função de espalhamento pelo método da divisão. M = {m}")
    df = resultsModHash(m, r)
    histo = df['Hashing results'].value_counts()
    #df = pd.DataFrame({'hash_result':histo.index, 'count':histo.values})
    print(histo)
    save_df(df['Hashing results'], f"{m}_{r}")
    save_df(df, f"{m}_{r}_W_index")

def analysingMultHash():
    m = 200
    a = 0.62
    print(f"Primeira demonstração da função de espalhamento pelo método da divisão. M = {m}; A = {a}")
    df = resultsMultHash(m, a)
    histo = df['Hashing results'].value_counts()
    #df = pd.DataFrame({'hash_result':histo.index, 'count':histo.values})
    print(histo)
    save_df(histo, f"{m}_{a}", True)
    save_df(df, f"{m}_{a}_W_index")

    print("\n===========================================================\n")

    m = 200
    a = 0.61803398875
    print(f"Demonstração da função de espalhamento pelo método da divisão. M = {m}; A = {a}")
    df = resultsMultHash(m, a)
    histo = df['Hashing results'].value_counts()
    #df = pd.DataFrame({'hash_result':histo.index, 'count':histo.values})
    print(histo)
    save_df(histo, f"{m}_{a}", True)
    save_df(df, f"{m}_{a}_W_index")
    

def resultsMultHash(m, a):    
    d = {'Hashing key': [], 'Hashing results': []}
    for x in range(0, 500000):
        d['Hashing key'].append(x)        
        d['Hashing results'].append(hashFunctionByMult(x, m, a))
    return pd.DataFrame(data=d)

def resultsModHash(m, r):
    d = {'Hashing key': [], 'Hashing results': []}
    for x in range(0, r):
        d['Hashing key'].append(x)   
        d['Hashing results'].append(hashFunctionByMod(x, m))        
    return pd.DataFrame(data=d)

"""df = pd.DataFrame(data=d)
    df.hist(bins=25)
    plt.savefig(HERE + '/imgs/A62Hist.png') 
    print(df.value_counts())
    print(f"Histrograma completo em: {HERE}/imgs/A{math.floor(a % 100)}Hist.png")"""

def ploting(df, name, _bins = 25):
    plt.close("all")
    plt.figure()
    plot = df.plot.hist(bins = 10)
    plt.savefig(fname=name)

def path_of_img(img):
    return f"{HERE}/imgs/{img}.png"

def save_df(df, name, index=False):
    df.to_csv(f"{HERE}/dataframe_out/{name}.csv", index=index)