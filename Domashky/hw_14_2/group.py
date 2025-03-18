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
