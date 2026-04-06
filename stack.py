
from typing import Any


class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        return self.__elements.pop()
    
    def show(self):
        print(self.__elements)


pila = Stack()

pila.push(1)
pila.show()
pila.push(2)
pila.show()

pila.push(3)
pila.show()
aux = pila.pop()
pila.push(4)
pila.show()