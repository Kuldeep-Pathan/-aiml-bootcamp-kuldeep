from itertools import combinations, permutations, product

# -----------------------------------
# TASK 03 - Combinations with itertools
# -----------------------------------

students = ["Asha", "Ravi", "Meera", "Dev", "Priya"]

# -----------------------------------
# 1. Generate every possible pair
# -----------------------------------

pairs = list(combinations(students, 2))

print("Student pairs:")
for pair in pairs:
    print(pair)

print("\nTotal pairs:", len(pairs))

# Formula:
# nCr = n! / (r! * (n-r)!)
# 5C2 = 5! / (2! * 3!) = 10


# -----------------------------------
# 2. Ordered pairs using permutations
# -----------------------------------

ordered_pairs = list(permutations(students, 2))

print("\nOrdered pairs:")
for pair in ordered_pairs:
    print(pair)

print("\nTotal ordered pairs:", len(ordered_pairs))

# Permutations give a larger count because order matters.
# (Asha, Ravi) and (Ravi, Asha) are different.


# -----------------------------------
# 3. Shirt colours and sizes using product
# -----------------------------------

colors = ["Red", "Blue", "Black"]
sizes = ["M", "L"]

shirt_options = list(product(colors, sizes))

print("\nShirt combinations:")
for option in shirt_options:
    print(option)


# -----------------------------------
# 4. All feature subsets
# -----------------------------------

features = ["Age", "Salary", "Experience", "Education"]

all_subsets = []

for r in range(len(features) + 1):
    subsets = combinations(features, r)

    for subset in subsets:
        all_subsets.append(subset)

print("\nAll feature subsets:")
for subset in all_subsets:
    print(subset)

print("\nTotal subsets:", len(all_subsets))

# Formula:
# Total subsets = 2^n
# Here n = 4
# 2^4 = 16