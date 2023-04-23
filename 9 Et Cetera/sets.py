students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclow"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "ron", "house": "Gryffindor"},
    {"name": "hermione", "house": "Gryffindor"}
]

# We dont use append on sets, we use add
houses = set()
for student in students:
    houses.add(student["house"])
    
for house in sorted(houses):
    print(house)