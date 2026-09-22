def class_average(students, passing=40):
    total = 0
    passed = 0

    for s in students:
        breakpoint()

        total = s["marks"]
        if s["marks"] > passing:
            passed += 1

    average = total / len(students)
    pass_rate = passed / len(students) * 100

    return average, pass_rate


data = [
    {"name": "asha",  "marks": 88},
    {"name": "ravi",  "marks": 92},
    {"name": "meera", "marks": 79},
    {"name": "dev",   "marks": 40},
]

avg, rate = class_average(data)

print(f"average: {avg}")
print(f"pass rate: {rate}%")


'''# Bug 1: The total was being overwritten with each student's marks.
# PDB showed that total changed from 88 to 92 instead of accumulating.
# Changed '=' to '+=' to add each student's marks to the total.
total += s["marks"]'''

'''# Bug 2: '>' did not count a student who scored exactly the passing mark.
# PDB showed that Dev's score was 40, but 40 > 40 was False.
# Changed '>' to '>=' so a score equal to the passing mark is counted as passing.
if s["marks"] >= passing:
    passed += 1'''

'''def class_average(students, passing=40):
    total = 0
    passed = 0

    for s in students:
        # Bug 1: total was overwritten with each student's marks.
        # PDB showed that total became 88, then 92, then 79, then 40.
        # It should add each student's marks instead.
        total += s["marks"]

        # Bug 2: '>' did not count a student who scored exactly 40.
        # PDB showed that Dev had 40 marks, but 40 > 40 was False.
        # '>=' is needed because 40 is the passing mark.
        if s["marks"] >= passing:
            passed += 1

    # Bug 3: The average was wrong because total contained only the
    # last student's marks due to Bug 1. After fixing total += above,
    # PDB showed that total became 299, giving the correct average 74.75.
    average = total / len(students)

    pass_rate = passed / len(students) * 100

    return average, pass_rate==


data = [
    {"name": "asha",  "marks": 88},
    {"name": "ravi",  "marks": 92},
    {"name": "meera", "marks": 79},
    {"name": "dev",   "marks": 40},
]

avg, rate = class_average(data)

print(f"average: {avg}")
print(f"pass rate: {rate}%")'''