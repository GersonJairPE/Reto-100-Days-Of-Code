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

# Decorador

def upperCase_decorator(function):
    def wrapper():
        func = function()
        poner_mayusculas = func.upper()
        return poner_mayusculas
    return wrapper 

# SIN USAR UN DECORADOR
def saludo():
    return 'Hola mundo'

g = upperCase_decorator(saludo)
g()

# USANDO EL DECORADOR
@upperCase_decorator
def presentacion():
    return 'Hola soy gerson pereyra'

presentacion()

# Decorador con parametros

def decorador(function):
    def wrapper(*args, **kwargs):
        print("Esta es la funcion decorada\n")
        resultado = function(*args, **kwargs)
        print("Fin de la decoracion")
        
        return resultado
    return wrapper


@decorador
def suma(a, b):
    return a+b

print(suma(2, 20))

# decorador

def separador(function):
    def wrapper():
        res = function()
        return res.split()
    return wrapper

# se ejecuta de abajo hacia arriba
@separador
@upperCase_decorator
def presentacion():
    return 'Hola soy gerson pereyra'

presentacion()


['asdasd','asdasd'].upper()

# =============================================================================
# FUNCION MAP

def factorial(n):
    i=1
    p=1
    while i<=n:
        p*=i
        i+=1
    return 

print(list(map(factorial, [1,2,3,4,5])))

lista=['1','2','3','4','5']
print(list(map(int, lista)))

# FUNCION MAP CON FUNCION LAMBDA

print(list(map(lambda x: x**2, [1,2,3,4,5])))

print(list(map(lambda x: x.upper(), ['g','e','r','s','o','n'])))

# =============================================================================
# FUNCION FILTRO
# funcion que muestra los elementos que cumplen la condicion de una funcion 
# que devuelve un booleano

numbers = [1, 2, 3, 4, 5]


def es_par(num):
    if num % 2 ==0:
        return True
    return False

fn = filter(es_par, numbers)
print(list(fn))


def es_impar(num):
    if num%2 != 0:
        return True
    return False

fn2 = filter(es_impar, numbers)
print(list(fn2))


numeros = [i for i in range(1,101)]


# filtrar los multiplos de 7

def es_multp_7(num):
    if num%7==0:
        return True
    return False

fn3 = filter(es_multp_7, numeros)
print(list(fn3))


# =============================================================================
# FUNCION REDUCE

def suma(a,b):
    return int(a)+int(b)

fn4 = reduce(suma, numeros)
print(list(fn4))
