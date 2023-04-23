students = [
    {"name": "harry", "house": "gryffindor"},
    {"name": "cho", "house": "ravenclaw"},
    {"name": "draco", "house": "slytherin"},
    {"name": "hermione", "house": "gryffindor"},
    {"name": "luna", "house": "ravenclaw"},
    {"name": "neville", "house": "gryffindor"},
    {"name": "pansy", "house": "slytherin"},
    {"name": "ron", "house": "gryffindor"},
    {"name": "seamus", "house": "gryffindor"},
    {"name": "trevor", "house": "slytherin"},
]


def is_griffindor(student):
    return student["house"] == "gryffindor"


gryffindors = filter(is_griffindor, students)
for student in sorted(gryffindors, key=lambda student: student["name"]):
    print(student["name"])
