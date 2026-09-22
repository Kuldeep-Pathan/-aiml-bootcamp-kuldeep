# Write a script that generates a text file with 500,000 lines. (A loop and a write is fine.)

with open("data.txt", "w") as file:
    for i in range(500000):
        file.write(f"Line {i + 1}\n")

print("500,000 lines created.")


# Read it back and count the lines — without ever calling .read()

with open("data.txt", "r") as file:
    count = 0

    for line in file:
        count += 1

print("Number of lines:", count)


# Use with open(...). Do not call .close() yourself.

with open("data.txt", "r") as file:
    count = 0

    for line in file:
        count += 1

print("Number of lines:", count)



# Count how many lines contain a particular word.


count = 0

with open("data.txt", "r") as file:
    for line in file:
        if "Line" in line:
            count += 1

print("Lines containing 'Line':", count)


#  Bonus: do the same thing with a CSV using the csv module.


import csv

count = 0

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        if "Python" in row:
            count += 1

print("CSV matches:", count)



#  a JSON file with json.

import json

with open("data.json", "r") as file:
    data = json.load(file)

count = 0

for item in data:
    if "Python" in str(item):
        count += 1

print("JSON matches:", count)


'''Note: CSV is read row-by-row, while json.load() loads the JSON data into memory.'''

'''1. What does with guarantee? What is a context manager?

with automatically manages resources and closes the file even if an error occurs. A context manager handles setup and cleanup automatically.

2. Difference between read(), readline(), and readlines()?
read() → reads the whole file.
readline() → reads one line.
readlines() → reads all lines into a list.

3. Why not parse CSV by splitting on commas?
Because a value can contain a comma inside quotes.'''