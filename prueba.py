


def secuencial(buscado, values):
    for i in range(len(values)):            # O(N * N)
        for j in range(len(values)):        # O(N)
            print(i)

    return -1



# secuencial O(3)
print('hola')   # O(1)
a = 1 + 2       # O(1)
print('chau')   # O(1)


# condicional

if a > 10 and a != 100:                              # O(3) +  O(6) ->   O(9)
    print('hola')   # O(1)
    a = 1 + 2       # O(1)
    print('chau')   # O(1)
    print('hola')   # O(1)
    a = 1 + 2       # O(1)
    print('chau')   # O(1)
else:
    print('hola')   # O(1)
    a = 1 + 2       # O(1)
    print('chau')   # O(1)


# ciclo for
for i in range(20):           #  O(20 * 6)
    print('hola')   # O(1)
    a = 1 + 2       # O(1)
    print('chau')   # O(1)
    print('hola')   # O(1)
    a = 1 + 2       # O(1)
    print('chau')   # O(1)


while i < 20:           #  O(20 * 6)
    print('hola')   # O(1)
    a = 1 + 2       # O(1)
    print('chau')   # O(1)
    print('hola')   # O(1)
    a = 1 + 2       # O(1)
    print('chau')   # O(1)