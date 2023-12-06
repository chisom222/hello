people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)