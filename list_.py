from typing import Any

class List(list):
    
    def show(self) -> None:
        for element in self:
            print(element)
    
    def search(self, search_value: Any):
        
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            value = self[middle]

            if value.nom == search_value:
                return middle
            elif value.nom < search_value:
                start = middle + 1
            else:
                end = middle -1
            
            middle = (start + end) // 2

l = List()

# l.append(1)
# l.append(3)
# l.append(5)
# l.append(7)

# print(l.search(5))
# print(l.search(17))


class Persona:

    def __init__(self, nom, ape, edad):
        self.nom = nom
        self.ape = ape
        self.edad = edad

    def __str__(self):
        return f"{self.ape} {self.nom} {self.edad}"


l.append(Persona("Ana", "Blanc", 42))
l.append(Persona("Dario", "Aron", 12))
l.append(Persona("Juan", "Perez", 24))

# def by_name(item):
#     return item.nom

# def by_last_name(item):
#     return item.ape

# def by_age(item):
#     return item.edad


# l.sort(key=by_age)

print(l.search("Dario"))

l.show()
