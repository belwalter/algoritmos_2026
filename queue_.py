from typing import Any

class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None: 
        self.__elements.append(value)

    def attention(self) -> Any:
        return self.__elements.pop(0)

    def size(self) -> int:
        return len(self.__elements)

    def on_front(self) -> Any:
        return self.__elements[0]

    def move_to_end(self) -> Any:
        value = self.__elements.pop(0)
        self.__elements.append(value)
        return value

    def show(self) -> None:
        for i in range(len(self.__elements)):
            value = self.move_to_end()
            print(value)
