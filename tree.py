
from typing import Any, Optional

class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values


class BinaryTree():

    def __init__(self):
        self.root = None

    def insert_node(self, value: Any, other_value: None) -> None:

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
            print(root.value)
            aux = None
            if root.right is None:
                print('mayor encontrado')
                return root.left, root
            else:
                print('segui buscando a la derecha')
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            if root is not None:
                if value < root.value:
                    print('ir a la izq')
                    input()
                    root.left, x = __delete_node(root.left,value)
                elif value > root.value:
                    print('ir a la derecha')
                    input()
                    root.right, x = __delete_node(root.right, value)
                else:
                    print('valor encontrado')
                    input()
                    x = root.value
                    aux = None
                    if root.left is None:
                        print('no tiene hijo izquierdo')
                        input()
                        return root.right
                    elif root.right is None:
                        print('no tiene hijo derecho')
                        input()
                        return root.left
                    else:
                        print('buscar remplazo')
                        input()
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
            return root, x

        x = None
        self.root, x = __delete_node(self.root, value)

        return x

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



class Persona:

    def __init__(self, nom, ape, dni):
        self.nom = nom
        self.ape = ape
        self.dni = dni

    def __str__(self):
        return f"{self.ape} {self.nom} {self.dni}"

arbol = BinaryTree()
arbol_ape = BinaryTree()

p1 = Persona('Pepito', 'Gonzalez', 23)
p2 = Persona('Pepito', 'Perez', 24)
p3 = Persona('Pepito', 'Garcia', 25)
p4 = Persona('Pepito', 'Casanova', 26)

arbol.insert_node(p1.dni, p1)
arbol.insert_node(p2.dni, p2)
arbol.insert_node(p3.dni, p3)
arbol.insert_node(p4.dni, p4)

arbol_ape.insert_node(p1.ape, p1)
arbol_ape.insert_node(p2.ape, p2)
arbol_ape.insert_node(p3.ape, p3)
arbol_ape.insert_node(p4.ape, p4)
# arbol.insert_node('F')
# arbol.insert_node('B')
# arbol.insert_node('K')
# arbol.insert_node('E')
# arbol.insert_node('H')
# arbol.insert_node('R')
# arbol.insert_node('G')



# print(arbol.root.right.left.value)

# arbol.inorden()

# print()
# print('eliminar', arbol.delete_node('F'))
# print()
# arbol.inorden()

aux = arbol.search(26)
if aux is not None:
    print(f'valor encontrado {aux.other_values}')
else:
    print('no encontrado')

aux = arbol_ape.search('Gonzalez')
if aux is not None:
    print(f'valor encontrado {aux.other_values}')
else:
    print('no encontrado')