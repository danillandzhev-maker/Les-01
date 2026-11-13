"""Run the assignment checks: python main.py"""

from group import Group, TooManyStudentsError
from student import Student


def main():
    st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
    st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
    gr = Group("PD1")
    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)

    assert gr.find_student("Jobs") == st1
    assert gr.find_student("Jobs2") is None

    gr.delete_student("Taylor")
    print("\nAfter deleting Taylor:")
    print(gr)
    assert len(gr.students) == 1

    # Also retain the previous homework requirement: catch the custom error
    # outside Group when trying to add student number eleven.
    limited_group = Group("LIMIT")
    try:
        for number in range(1, 12):
            limited_group.add_student(
                Student("Unknown", 18, f"Student{number}", "Example", f"ID{number}")
            )
    except TooManyStudentsError as error:
        print(f"\nПеревірка ліміту: {error}")
    else:
        raise AssertionError("Додавання 11-го студента мало викликати помилку")
    assert len(limited_group.students) == 10
    print("Усі перевірки пройдено.")


if __name__ == "__main__":
    main()
