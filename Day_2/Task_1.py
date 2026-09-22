#Student Class

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = []

student = Student("Rahul", 101)

print(student.name)
print(student.roll)
print(student.marks)



#Student Class with __init__ 

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []


student = Student("Rahul", 101)

print(student.name)
print(student.roll_number)
print(student.marks)


# Add add_mark(score) that appends to the list

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_mark(self, score):
        self.marks.append(score)


student = Student("Rahul", 101)

student.add_mark(85)
student.add_mark(90)

print(student.name)
print(student.roll_number)
print(student.marks)


# Add average() that returns the mean 

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_mark(self, score):
        self.marks.append(score)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)


student = Student("Rahul", 101)

student.add_mark(80)
student.add_mark(90)

print(student.marks)
print(student.average())


# Add highest() and lowest()

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_mark(self, score):
        self.marks.append(score)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def highest(self):
        if len(self.marks) == 0:
            return 0
        return max(self.marks)

    def lowest(self):
        if len(self.marks) == 0:
            return 0
        return min(self.marks)


student = Student("Rahul", 101)

student.add_mark(80)
student.add_mark(90)
student.add_mark(75)

print("Highest:", student.highest())
print("Lowest:", student.lowest())



#  Create three students, give them marks

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_mark(self, score):
        self.marks.append(score)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)


student1 = Student("Rahul", 101)
student2 = Student("Amit", 102)
student3 = Student("Ravi", 103)

student1.add_mark(80)
student1.add_mark(90)

student2.add_mark(70)
student2.add_mark(80)

student3.add_mark(90)
student3.add_mark(100)

print(student1.name, student1.average())
print(student2.name, student2.average())
print(student3.name, student3.average())


'''1. What happens when you write Student("Asha", 12)?
Python creates a Student object and automatically calls the __init__() method.

2. What happens if you delete self from a method?
You get a TypeError because Python automatically passes the object as the first argument.

3. Why put self.marks = [] inside __init__?
Because each student needs a separate marks list. At class level, 
the same list would be shared by all students.'''



