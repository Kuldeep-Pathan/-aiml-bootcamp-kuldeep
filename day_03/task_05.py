from collections import defaultdict, namedtuple, deque, Counter


# ============================================================
# TASK 05 - Collections Bake-Off
# ============================================================


# ------------------------------------------------------------
# 1. defaultdict - Group employees by department
# ------------------------------------------------------------

employees = [
    ("IT", "Rahul"),
    ("HR", "Priya"),
    ("IT", "Amit"),
    ("Finance", "Neha"),
    ("HR", "Riya"),
    ("IT", "Karan")
]

departments = defaultdict(list)

for department, employee in employees:
    departments[department].append(employee)

print("Employees by department:")
print(dict(departments))


# ------------------------------------------------------------
# 2. namedtuple - Name, Age, City
# ------------------------------------------------------------

Person = namedtuple("Person", ["name", "age", "city"])

people = [
    ("Rahul", 24, "Indore"),
    ("Priya", 23, "Pune"),
    ("Amit", 25, "Bhopal")
]

people_named = [Person(name, age, city) for name, age, city in people]

print("\nPeople:")
for p in people_named:
    print(p)
    print("City using p.city:", p.city)
    print("City using p[2]:", p[2])


# ------------------------------------------------------------
# 3. deque - Last 5 searches
# ------------------------------------------------------------

history = deque(maxlen=5)

searches = [
    "Python",
    "Java",
    "Spring Boot",
    "SQL",
    "AI",
    "Machine Learning"
]

for search in searches:
    history.append(search)

print("\nLast 5 searches:")
print(history)


# ------------------------------------------------------------
# 4. Counter - Common and different words
# ------------------------------------------------------------

text1 = "python java sql python ai"
text2 = "python sql machine learning ai"

words1 = Counter(text1.split())
words2 = Counter(text2.split())

common_words = words1 & words2
only_in_text1 = words1 - words2
only_in_text2 = words2 - words1

print("\nCommon words:")
print(common_words)

print("\nWords only in text 1:")
print(only_in_text1)

print("\nWords only in text 2:")
print(only_in_text2)

print("\nCounter operations:")
print("c1 - c2:", words1 - words2)
print("c1 & c2:", words1 & words2)
print("c1 | c2:", words1 | words2)