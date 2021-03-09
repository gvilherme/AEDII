import math

def hashFunctionByMod(key, m):
    return key % m

def hashFunctionByMult(key, m, A = 0.62):
    return math.floor(m * ((key * A) % 1))