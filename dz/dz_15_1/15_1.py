
class TooManyStudentsError(Exception):
    pass


class Student:
    def __init__(self, name):
        self.name = name


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise TooManyStudentsError("У групі не може бути більше 10 студентів")
        self.students.append(student)


group = Group()

try:
    for number in range(1, 12):
        student = Student(f"Student {number}")
        group.add_student(student)
        print(f"{student.name} доданий до групи")

except TooManyStudentsError as error:
    print(error)
