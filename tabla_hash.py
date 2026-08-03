from random import choice, randint


table_legion = [None] * 15
table_id = [None] * 1000

legions = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

def hash_id(clave: int) -> int:

    return clave % 1000

def hash_legion(clave: str) -> int:
    h = 0
    for caracter in clave:
        h = h * 33 + ord(caracter)

    return h % 15

# for legion in legions:
#     print(legion, hash_legion(legion))


for i in range(12000):
    trooper = f'{choice(legions)}-{randint(1000, 9999)}'
    
    index = hash_legion(trooper[:2])
    index_id = hash_id(int(trooper[3:]))

    if table_id[index_id] is None:
        table_id[index_id] = []

    if table_legion[index] is None:
        table_legion[index] = []

    table_id[index_id].append(trooper)
    table_legion[index].append(trooper)

# print(table_legion)

# index = hash_legion('TF')
index_id = hash_id(781)

# print(len(table_legion[index]))

for trooper in table_id[index_id]:
    print(trooper)