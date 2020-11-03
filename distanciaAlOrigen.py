from math import sqrt, pow

def distanciaAlOrigen(disparoX, disparoY):
    
    ubicacionDisparo = round(sqrt(pow(disparoX,2) + pow(disparoY, 2)),2)
    
    return ubicacionDisparo