#importamos el modulo creado como archivo

# from module1 import  welcomeToModules, suma_numbers

# cambiamos de nombre a las funciones

from module1 import  welcomeToModules as wtm, suma_numbers as sn

'''
- Tareas que se pueden realizar:
- crear
- cambiar el directorio de trabajo actual
- eliminar un directorio (carpeta)
- recuperar su contenido
- cambiar directorio actual
- identificar el directorio actual.
'''

import os # permite realizar acciones con el sistema ya sea crear carpetas 

'''
print()
welcomeToModules('Gerson Pereyra')
print()
print('Segunda funcion')
print()
val = suma_numbers(2,3)
print(val)
'''

'''
wtm('GERJPE')
print(sn(56, 67))
'''


# os.mkdir('newFolder') # creando carpeta dentro del directorio actual
# os.chdir('newFolder') # cambiando el directorio actual
# os.getcwd() # se obtiene el directorio de trabajo actual
# os.rmdir('newFolder')