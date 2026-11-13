"""Group model with a maximum of ten students."""

from student import Student


class TooManyStudentsError(Exception):
    """Raised when adding a student would exceed the group limit."""


class Group:
    MAX_STUDENTS = 10

    def __init__(self, group_name):
        self.group_name = group_name
        self.students = set()

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("До групи можна додавати лише об'єкти Student")
        if student in self.students:
            return
        if len(self.students) >= self.MAX_STUDENTS:
            raise TooManyStudentsError("У групі не може бути більше 10 студентів")
        self.students.add(student)

    def find_student(self, last_name):
        for student in self.students:
            if last_name in student.last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.students.remove(student)

    def __str__(self):
        students = "\n".join(str(student) for student in sorted(
            self.students, key=lambda item: (item.last_name, item.first_name)
        ))
        return f"Group {self.group_name}:\n{students or '(немає студентів)'}"
