# -*- coding: utf-8 -*-
"""01_Variables.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TxfP3t4Iz-LENDssrqNShYd7Isj9Me8K
"""

from ctypes import addressof
from os import name
### variables ###

#my_string_variable = "my string variable"
#print(my_string_variable)

#my_int_variable = 5
#print(my_int_variable)

#my_int_to_str_variable = str(my_int_variable)
#print(my_int_to_str_variable)
#print(type(my_int_to_str_variable))

#my_bool_variable = False
#print(my_bool_variable)

#concatenacion de variables en un print
#print(my_string_variable, my_int_to_str_variable, my_bool_variable)
#print("este es el valor de:", my_bool_variable)

# algunos funciones del sistema
#print(len(my_string_variable))

# Variables en una sola linea. !Cuidado conn abusar de esta sintaxis¡

#name, surname, alias, age = "grupo", "Programacion", 'CECyTEM', 35
#print("Me llamo:", name, surname, "Mi edad es:",
#      age, "Y mi alias es:", alias)

# Inputs
#name = input("¿Cual es tu nombre?" )
#age = input("¿cuantos años tienes?" )
#print(name)
#print(age)

# cambiamos tu tipo
#name=15
#age = "Carlos"
#print(name)
#print(age)

# ¿Forzamos el tipo?
address: str = "Mi direccion"
address = True
address = 5
address =1.2
print(type(address))