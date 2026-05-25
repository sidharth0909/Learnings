from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name': 'Sidharth', 'age': 24}
new_person1: Person = {'name': 'Shrey', 'age': '23'}

print(new_person)
print(new_person1)