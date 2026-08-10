
from typing import Any

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

arbol.insert_node('H')
arbol.insert_node('M')
arbol.insert_node('D')
arbol.insert_node('L')
arbol.insert_node('A')
arbol.insert_node('Z')


# print(arbol.root.right.left.value)

arbol.postorden()