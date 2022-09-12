# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 23:13:13 2022

@author: GERSON
"""

# TIPOS DE ERRORES

# Error de sintaxis (SyntaxError)
print 'hello world'

print('hello world')

# Error de nombre (nameError)

print(age)

arreglando
age = 10
print(age)

# Error por indice

f =[1,2,3]
f[4]


# Error por modulos no encontrados

import asdad

# Error por atributo

import math
# math.PI

math.pi


# ERROR POR CLAVE

users = {'name':'Asab', 'age':250, 'country':'Finland'}
# users['namce']

users['name']

# ERROR POR TIPO DE DATO
#4 + '4'
4 + float('4')

# IMPORT ERROR

# from math import power
# power(2,3)

from math import pow

pow(2,3)

# VALUERROR

# int('12a')

# ZeroDivisionError
0/0