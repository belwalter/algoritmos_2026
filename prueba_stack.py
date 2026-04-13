from random import randint

from stack import Stack


# pila = Stack()

# for i in range(10):
#     pila.push(randint(1, 10))

# print()
# pila.show()
# print()

# search_value = int(input('ingrese un numero para contar ocurrencias '))
# counter = 0

# while pila.size() > 0:
#     value = pila.pop()
#     if value == search_value:
#         counter += 1
    
# print(f'cantidad de ocurrencias de {search_value} en la pila: {counter}')

pila = Stack()

for i in range(10):
    pila.push(randint(1, 10))

print()
pila.show()
print()

pila_aux = Stack()

while pila.size() > 0:
    value = pila.pop()
    if value % 2 == 0:
        pila_aux.push(value)

while pila_aux.size() > 0:
    value = pila_aux.pop()
    pila.push(value)

pila.show()
