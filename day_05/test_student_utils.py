from student_utils import Student


def test_student_creation():
    student = Student("Asha", 101)

    assert student.name == "Asha"
    assert student.roll_number == 101
    assert student.marks == []


def test_add_mark():
    student = Student("Asha", 101)

    student.add_mark(80)
    student.add_mark(90)

    assert student.marks == [80, 90]


def test_average_with_marks():
    student = Student("Asha", 101)

    student.add_mark(80)
    student.add_mark(90)

    assert student.average() == 85.0


def test_average_without_marks():
    student = Student("Asha", 101)

    assert student.average() == 0.0


def test_highest_mark():
    student = Student("Asha", 101)

    student.add_mark(70)
    student.add_mark(95)
    student.add_mark(80)

    assert student.highest_mark() == 95


def test_highest_mark_without_marks():
    student = Student("Asha", 101)

    assert student.highest_mark() is None


def test_lowest_mark():
    student = Student("Asha", 101)

    student.add_mark(70)
    student.add_mark(95)
    student.add_mark(80)

    assert student.lowest_mark() == 70


def test_lowest_mark_without_marks():
    student = Student("Asha", 101)

    assert student.lowest_mark() is None


def test_string_representation():
    student = Student("Asha", 101)

    assert str(student) == "Student(name=Asha, roll_number=101)"


def test_repr_representation():
    student = Student("Asha", 101)

    assert repr(student) == "Student(name='Asha', roll_number=101)"
