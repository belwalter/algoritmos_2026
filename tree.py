
from typing import Any, Optional

from queue_ import Queue
class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
    
    def __str__(self):
        return self.value


class BinaryTree():

    def __init__(self):
        self.root = None

    def insert_node(self, value: Any, other_value=None) -> None:

        def __insert_node(root, value, other_value=None):
            if root is None:
                # print(f'lugar vacio insertar {value}')
                root = Node(value, other_value)
            elif value < root.value:
                # print(f'ir a la izquierda de {root.value}')
                root.left = __insert_node(root.left, value, other_value)
            else:
                # print(f'ir a la derecha de {root.value}')
                root.right = __insert_node(root.right, value, other_value)
            
            return root
            
        self.root = __insert_node(self.root, value, other_value)

    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            # print(root.value)
            aux = None
            if root.right is None:
                # print('mayor encontrado')
                return root.left, root
            else:
                # print('segui buscando a la derecha')
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    # print('ir a la izq')
                    # input()
                    root.left, x, other_value = __delete_node(root.left,value)
                elif value > root.value:
                    # print('ir a la derecha')
                    # input()
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    # print('valor encontrado')
                    # input()
                    x = root.value
                    other_value = root.other_values
                    aux = None
                    if root.left is None:
                        # print('no tiene hijo izquierdo')
                        # input()
                        return root.right, x, other_value
                    elif root.right is None:
                        # print('no tiene hijo derecho')
                        # input()
                        return root.left, x, other_value
                    else:
                        # print('buscar remplazo')
                        # input()
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
            return root, x, other_value

        other_value = None
        self.root, x, other_value = __delete_node(self.root, value)

        return x, other_value

    def search(self, value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:
            
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)

            return aux


        node = __search(self.root, value)
        
        return node 

    def inorden(self) -> None:
        
        def __inorden(root):
            if root.left is not None:
                # print(f'anda a la izquierda de {root.value}')
                __inorden(root.left)
            # print(f'procesa nodo actual')
            print(root.value)
            if root.right is not None:
                # print(f'anda a a derecha de {root.value}')
                __inorden(root.right)

        __inorden(self.root)
    
    def postorden(self) -> None:
        
        def __postorden(root):
            if root.right is not None:
                __postorden(root.right)
            print(root.value)
            if root.left is not None:
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self) -> None:
        def __preorden(root):
            print(root.value)
            if root.left is not None:
                __preorden(root.left)
            if root.right is not None:
                __preorden(root.right)

        __preorden(self.root)

    def by_level(self) -> None:

        pendings = Queue()

        if self.root is not None:
            pendings.arrive(self.root)
            # print(f'queue')
            # pendings.show()
            # input()
            while pendings.size() > 0:
                node = pendings.attention()
                print(node.value)
                # input()
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)
                # print(f'queue ')
                # pendings.show()
                # input()

    def inorden_villain(self) -> None:
        
        def __inorden_villain(root):
            if root.left is not None:
                __inorden_villain(root.left)
            if root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_villain(root.right)

    def postorden_hero(self):
    
        def __postorden_hero(root):
            if root.right is not None:
                __postorden_hero(root.right)
            if not root.other_values['is_villain']:
                print(root.value)
            if root.left is not None:
                __postorden_hero(root.left)

        __postorden_hero(self.root)

    def inorden_hero_star_with(self, prefix: str) -> None:
        
        def __inorden_hero_star_with(root, prefix):
            if root.left is not None:
                __inorden_hero_star_with(root.left, prefix)
            if root.value.startswith(prefix) and not root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_hero_star_with(root.right, prefix)

        __inorden_hero_star_with(self.root, prefix)

    def proxy_search(self, prefix: str) -> None:
        
        def __proxy_search(root, prefix):
            if root.left is not None:
                __proxy_search(root.left, prefix)
            if prefix in root.value.lower():
                print(root.value)
            if root.right is not None:
                __proxy_search(root.right, prefix)

        __proxy_search(self.root, prefix)

    def count_heroes(self) -> None:
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.left is not None:
                    count += __count_heroes(root.left)
                if not root.other_values['is_villain']:
                    count += 1
                if root.right is not None:
                    count += __count_heroes(root.right)
            return count

        count = __count_heroes(self.root)
        return count

# class Persona:

#     def __init__(self, nom, ape, dni):
#         self.nom = nom
#         self.ape = ape
#         self.dni = dni

#     def __str__(self):
#         return f"{self.ape} {self.nom} {self.dni}"

# arbol = BinaryTree()
# arbol_ape = BinaryTree()

# p1 = Persona('Pepito', 'Gonzalez', 23)
# p2 = Persona('Pepito', 'Perez', 24)
# p3 = Persona('Pepito', 'Garcia', 25)
# p4 = Persona('Pepito', 'Casanova', 26)

# arbol.insert_node(p1.dni, p1)
# arbol.insert_node(p2.dni, p2)
# arbol.insert_node(p3.dni, p3)
# arbol.insert_node(p4.dni, p4)

# arbol_ape.insert_node(p1.ape, p1)
# arbol_ape.insert_node(p2.ape, p2)
# arbol_ape.insert_node(p3.ape, p3)
# arbol_ape.insert_node(p4.ape, p4)
# arbol.insert_node('F')
# arbol.insert_node('B')
# arbol.insert_node('K')
# arbol.insert_node('E')
# arbol.insert_node('H')
# arbol.insert_node('R')
# arbol.insert_node('G')

# arbol.by_level()

# print(arbol.root.right.left.value)

# arbol.inorden()

# print()
# print('eliminar', arbol.delete_node('F'))
# print()
# arbol.inorden()

# aux = arbol.search(26)
# if aux is not None:
#     print(f'valor encontrado {aux.other_values}')
# else:
#     print('no encontrado')

# aux = arbol_ape.search('Gonzalez')
# if aux is not None:
#     print(f'valor encontrado {aux.other_values}')
# else:
#     print('no encontrado')