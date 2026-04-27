from copy import copy, deepcopy
from typing import Any


class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        return self.__elements.pop()
    
    def show(self) -> None:
        stack_aux = Stack()
        stack_aux.__elements = copy(self.__elements)

        while stack_aux.size() > 0: 
            value = stack_aux.pop()
            print(value)
        
        # stack_aux = Stack()

        # while self.size() > 0: 
        #     value = self.pop()
        #     print(value)
        #     stack_aux.push(value)
        
        # while stack_aux.size() > 0: 
        #     value = stack_aux.pop()
        #     self.push(value)
        
    def size(self) -> int:
        return len(self.__elements)
    
    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]
