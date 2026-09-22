# Print one of your students. Note the ugly output in a comment

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []


student1 = Student("Kuldeep", 101)

print(student1)

# Ugly output: <__main__.Student object at 0x...>



#  Add a __str__ method that returns something 

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def __str__(self):
        return f"Student: {self.name}, Roll Number: {self.roll_number}"


student1 = Student("Kuldeep", 101)

print(student1)


#  Print again. Confirm the difference

print(student1)

'''Before __str__:  
<__main__.Student object at 0x...> 

After __str__:
Student: Kuldeep, Roll Number: 101'''


# Now add __repr__ as well. Make it different from __str__

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def __str__(self):
        return f"Student: {self.name}, Roll Number: {self.roll_number}"

    def __repr__(self):
        return f"Student('{self.name}', {self.roll_number})"


student1 = Student("Kuldeep", 101)

print(student1)       # __str__
print(repr(student1)) # __repr__

'''__str__ → normal user-friendly output
__repr__ → developer-friendly representation'''



# Put a student inside a list and print the list. Which one gets used — __str__ or __repr__?

students = [student1]

print(students)

'''Observation: When an object is printed inside a list, Python uses __repr__, not __str__'''


'''1. What is the actual difference between __str__ and __repr__?
__str__ → user-friendly output.
__repr__ → developer/debugging output.


2. Why does printing a list not use __str__ on the items?
Because lists use __repr__ for their items.


3. What are two other dunder methods you could add to Student?
__eq__() → compare students.
__len__() → get the number of marks.'''

