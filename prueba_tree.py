
from super_heroes_data import superheroes
from tree import BinaryTree

class MarvelCharacter():

    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}"
    


arbol_marvel = BinaryTree()

print(f'cantidad de elementos {len(superheroes)}')
#A
for marvel_character in superheroes:
    arbol_marvel.insert_node(marvel_character['name'], other_value=marvel_character)

# #B
# arbol_marvel.inorden_villain()


# #C
# arbol_marvel.inorden_hero_star_with('An')

# #D
# print(f'cantidad de heroes: {arbol_marvel.count_heroes()}')

# E
search_str = input('ingrese lo que quiere buscar: ')
arbol_marvel.proxy_search(search_str.lower())

search_str = input('ingrese lo que quiere modificar: ')

node = arbol_marvel.search(search_str)
if node is not None:
    new_name = input('ingrese el nuevo nombre: ')
    delete_value, delete_other_value = arbol_marvel.delete_node(node.value)
    delete_other_value['name'] = new_name
    arbol_marvel.insert_node(new_name, delete_other_value)

print()
arbol_marvel.inorden_hero_star_with('D')

# # F
# arbol_marvel.postorden_hero()

#G