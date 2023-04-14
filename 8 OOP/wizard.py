class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing name')
        self.name = name

    def attack(self):
        print(f'attacking with power of {self.power}')


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Proffesor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


