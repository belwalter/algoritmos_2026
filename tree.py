
from typing import Any, Optional

class Node():

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():

    def __init__(self):
        self.root = None

    def insert_node(self, value: Any) -> None:

        def __insert_node(root, value):
            if root is None:
                # print(f'lugar vacio insertar {value}')
                root = Node(value)
            elif value < root.value:
                # print(f'ir a la izquierda de {root.value}')
                root.left = __insert_node(root.left, value)
            else:
                # print(f'ir a la derecha de {root.value}')
                root.right = __insert_node(root.right, value)
            
            return root
            
        self.root = __insert_node(self.root, value)

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


arbol = BinaryTree()

arbol.insert_node('F')
arbol.insert_node('B')
arbol.insert_node('K')
arbol.insert_node('E')
arbol.insert_node('H')
arbol.insert_node('R')
arbol.insert_node('G')



# print(arbol.root.right.left.value)

arbol.inorden()

print()
print('eliminar', arbol.delete_node('F'))
print()
arbol.inorden()