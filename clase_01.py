
print("hola mundo", "desde python")

# name = input('ingrese su nombre: ')
# print("su nombre es:", name)

# TIPOS DE DATOS PRIMITIVOS STR, INT, FLOAT, BOOL, NONE

variable = "Ana"
print(type(variable))
variable = 1234
print(type(variable))
variable = 12.5
print(type(variable))
variable = True
print(type(variable))
variable = None
print(type(variable))

# number = int(input('ingrese un numero: '))
# print(number + 100)

# funciones de conversion int, str, float, bool input('ingrese un numero: ')

# funciones aritmeticas +, -, *, /, //, %, **
# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(5 ** 2)

# asignacion = -->  a = 10

# secuencial
# condicional
# if-else | case
# operadores de control >, <, >=, <=, ==, != 

num = 5

if num > 5:
    print('es mayor')

    print('dentro del if')
print('fuera del if')

if num > 5:
    print('es mayor')
elif num < 5:
    print('es menor')
else:
    print('es 5')

control = True
if not control:
    print('se cumple el control')

# operadores logicos and or not ^
if num >= 5 and num <= 10:
    print('el numero esta entre 5 y 10')

num = 4
# match num:

#     case 1: print('es uno')
#     case 5: print('5')

#     case _: print('otro')


# ciclo
#     for | while
# num = 1
# while num < 5:
#     print(num)
#     num += 1 # num = num + 1

nums = [1, 2, 3, 4, 5]
nums.append(100)
# for i in range(len(nums)-1, 0, -1):
#     print(nums[i])
# for i in range(len(nums)):
#     print(nums[i])
# for index, elemento in enumerate(nums):
#     print('posicion:', index, 'valore:', elemento)
nums.reverse()
for num in nums:
    print(num)


# estruturas de datos list, dic, tuple


# num_list = [None] * 10
num_list =[]

print(type(num_list))
print(len(num_list))

num_list.append(1)
num_list.append(3)
num_list.append(7)
num_list.append(3)

# num_list.clear()
# print(num_list)
# print(num_list.count(9))
# # print(num_list.index(9))
# num_list.insert(21, 9)
# print(num_list)

# # print(num_list.pop(15))
# # print(num_list.remove(2))
# num_list.sort(reverse=True)
# num_list[4] = 100
# print(num_list)
# print(num_list[4])


# funciones y modulo
# var_global = 45

# def mi_funcion(num1, num2, otro = 'hola mundo', nuevo='otro valor'):
#     var_global = 123
#     print(otro)
#     print(nuevo)
#     print(var_global)
#     return num1 + num2, num1 - num2

# num1 = 5
# num2 = 3
# lista_nums = [1, 2, 3, 4]
# suma, diferencia = mi_funcion(num1, num2, nuevo='pepito')
# print(suma, diferencia)
# print(var_global)

# import
# import math

# from math import sqrt, factorial
from math import sqrt as raiz_cuadrada, factorial

from mi_modulo import suma, diferencia

print(raiz_cuadrada(16))
print(suma(5, '3'))
print(factorial())


# diccionarios clave -> valor
dic = {32: "juan", 45: "ana", 12: "pepe"}
print(type(dic))

print(dic.get(124))

print(dic.keys())
print(dic.values())
print(dic.items())

dic[99] = "maria"
dic[45] = 'Ana'


print('editado desde github web')
print('editado desde github web cambio 2')
