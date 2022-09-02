# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 21:59:39 2022

@author: GERSON
"""
language = 'Python'
lst = [i for i in language]
print(lst)

lista2 = [i for i in range(11)]
print(lista2)

lista3 = [i*i for i in range(50)]
print(lista3)

pares = [i for i in range(10) if i%2==0]
print(pares)

impares = [i for i in range(10) if i%2!=0]
print(impares)

values = [i for i in range(21) if i%2==0 and i>0]
print(values)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

values2 = [number for fila in list_of_lists for number in fila]
print(values2)


# FUNCION LAMBDA

MiFuncion = lambda v1, v2, v3: v1*v2+v3
MiFuncion(1, 2, 3)
###############################################################################

(lambda a,b: a*b)(4,3)
###############################################################################

def fun1(a):
    return lambda b: a+b

r = fun1(20)(3)
print(r)
###############################################################################

def fun2(c):
    return lambda s: c*s

print(fun2(4)(2))



# EJERCICIOS


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

c = [i for i in numbers if i <= 0]
c


list_of_lists_22 =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_uni = [n for row in list_of_lists_22 for n in row]

lista_uni