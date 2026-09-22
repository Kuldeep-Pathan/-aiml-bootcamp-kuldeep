#  Make a Person class with a name and a greet() method

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")


person1 = Person("Kuldeep")
person1.greet()


# Student inherit from Person. Use super().__init__() 

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


class Student(Person):
    def __init__(self, name, roll_number):
        super().__init__(name)
        self.roll_number = roll_number


student = Student("Kuldeep", 101)

student.greet()
print(student.roll_number)


#  Add a Teacher class that also inherits from Person but has a subject

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


class Student(Person):
    def __init__(self, name, roll_number):
        super().__init__(name)
        self.roll_number = roll_number


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


teacher = Teacher("Rahul", "Python")

teacher.greet()
print("Subject:", teacher.subject)


#  Override greet() in Student so it says something different


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


class Student(Person):
    def __init__(self, name, roll_number):
        super().__init__(name)
        self.roll_number = roll_number

    def greet(self):
        print("Hi, I am a student. My name is", self.name)


student = Student("Kuldeep", 101)

student.greet()


''' In a comment, argue one side: should Student inherit from Person, or just have a person? There is no single
right answer — defend your choice

Answer:-# Student should inherit from Person because a Student is a type of Person.
# This allows Student to reuse common properties and methods like name and greet().
# It also avoids repeating the same code.'''


'''1. What does super() do?
super() calls the parent class's method. Without it, the parent's initialization may not happen, 
so its attributes may be missing.

2. Why “composition over inheritance”?
Composition makes code more flexible and less tightly coupled,so it is often easier to change and maintain.

3. What is method overriding?
When a child class defines the same method as its parent with different behavior. 
The child's version is used for the child object.'''