# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 23:09:50 2022

@author: GERSON
"""
"""
import sys

print('hola {} espero te encuentres bien, estoy recibiendo el param {} y el param {} desde\
      la linea de comandos'.format(sys.argv[1], sys.argv[2], sys.argv[3]))


# comandos de sistema comunes

# sys.exit()

print()
print('-'*5)

print('El largo del valor es: ', sys.maxsize)
print()
print('-'*5)
print('La ubicación es ', sys.path)
print()
print('-'*5)
print('Python Version ', sys.version)


# MODULO DE ESTADISTICAS

from statistics import * # se wimportan todos los modulos estadisticos

Notas = [12,14,13,16,17,15,11,10,9,9,10]

print(mean(Notas))
print(median(Notas))
print(mode(Notas))
print(stdev(Notas))
"""

# MODULO MATEMATICO

from math import *
from math import floor as fl

#print(math.pi)
"""
try:
    print(math.sqrt(-1))
except:
    raise Exception("no se aceptan negativos")
"""
print(pow(3,2))
print(fl(4.556565))
print(ceil(4.2321323))
print(log10(100))


# MODULOS DE CADENA

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# MODULOS RANDOM

from random import randint, random

print(random())
print(randint(4, 20))


