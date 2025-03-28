class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise GrouplimitException('Group limit exceeded')

    def delete_student(self, last_name):
        if self.find_student(last_name) is not None:
            self.group.discard(self.find_student(last_name))
        else:
            print(f'No student {last_name}')

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Number: {self.number}\n{all_students}'


class GrouplimitException(Exception):
    pass


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st4 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st5 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st6 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st7 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st8 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st9 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st10 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st11 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st12 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')


gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
    gr.add_student(st12)
except GrouplimitException as err:
    print(err)

print(gr)

# Рішення викладача:
