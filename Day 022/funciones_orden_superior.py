# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 23:07:07 2022

@author: GERSON
"""

# FUNCIONES DE ORDEN SUPERIOR
# FUNCION NORMAL

def suma_lista(lista):
    return sum(lista)


# FUNCION DE ORDEN SUPERIOR

def applied_sum(f, valor):
    resultado = f(valor)
    return resultado
    
print(applied_sum(suma_lista, [6,7,8,9,4]))

# =============================================================================
# RETORNO DE FUNCIONES
# A devolver las funciones como valores de retorno de una funcion superior,
# se guardan en aguna variable apra ser aplicadas


def square(x):
    return x**2

def factorial(n):
    i=1
    p=1
    while i<=n:
        p*=i
        i+=1
    return p

# FUNCION DE ORDEN SUPERIOR


def superior_function(value):
    if value == 'square':
        return square 
    elif value == 'factorial':
        return factorial

function_returned = superior_function('factorial')
print(function_returned(5))


# =============================================================================
# FUNCIONES DE CIERRE
# es cuando usamos y definimos funciones dentro de otra funcion

def positividad_num():
    def verified(number):
        if number > 0:
            return print('Es positivo')
        elif number < 0:
            return print('Es negativo')
        else:
            return print('Es cero')
    return verified

verificador = positividad_num()

verificador(0)

# =============================================================================
# DECORADORES

# funcion normal

def welcome():
    return print('welcome to my house')

def upperCase_decorator(function):
    def wrapper():
        func = function()
        poner_mayusculas = func.upper()
        return poner_mayusculas
    return wrapper 

g = upperCase_decorator(welcome)
print(g())


'asdasdasd'.upper()
    










