import random

universal = input("Enter universal ")

universal_list = universal.split(',')

set_a = random.sample(universal_list, 5)
set_b = random.sample(universal_list, 5)

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

def union(set_a, set_b):
    concat = set_a + set_b

    result = []
    for i in range(len(concat)):
        if concat[i] not in result:
            result.append(concat[i])

    result.sort()
    return result

union_list = union(set_a, set_b)

print(f"Union: {union_list}")

def intersection(set_a, set_b):
    concat = set_a + set_b

    result = []

    for i in range(len(concat)):
        if concat[i] in set_a and concat[i] in set_b:
            if concat[i] not in result:
                result.append(concat[i])
    
    result.sort()
    return result

intersection_list = intersection(set_a, set_b)

print(f"Intersection: {intersection_list}")

def difference(set_a, set_b):
    concat = set_a + set_b

    result = []

    for element in concat:
        if element in set_a and element not in set_b:
            if element not in result:
                result.append(element)
    
    result.sort()
    return result

# al_set_a = [1, 2, 3, 4]
# al_set_b = [2, 4, 6, 7]

# difference_list = difference(al_set_a, al_set_b)
# print(difference_list)

def complement(universal, sets):
    result = []

    for element in universal:
        if element not in sets:
            result.append(element)

    result.sort()
    return result

al_universal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
al_set = [1, 2, 3, 4]

compelment_list = complement(al_universal, al_set)
print(f"Complement: {compelment_list}")

def symmetrical(set_a, set_b):
    concat = set_a + set_b
    result = []

    for element in concat:
        if (element in set_a and element not in set_b) or (element in set_b and element not in set_a):
            if element not in result:
                result.append(element)

    result.sort()
    return result

al_set_a = [1, 2, 3, 4, 5]
al_set_b = [0, 1, 2, 6, 7, 8]

symmetrical_list = symmetrical(al_set_a, al_set_b)
print(symmetrical_list)