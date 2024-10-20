def union(set_a, set_b):
    concat = set_a + set_b

    result = []
    for i in range(len(concat)):
        if concat[i] not in result:
            result.append(concat[i])

    result.sort()
    return result

def intersection(set_a, set_b):
    concat = set_a + set_b

    result = []

    for i in range(len(concat)):
        if concat[i] in set_a and concat[i] in set_b:
            if concat[i] not in result:
                result.append(concat[i])
    
    result.sort()
    return result

def difference(set_a, set_b):
    concat = set_a + set_b

    result = []

    for element in concat:
        if element in set_a and element not in set_b:
            if element not in result:
                result.append(element)
    
    result.sort()
    return result

def complement(universal, sets):
    result = []

    for element in universal:
        if element not in sets:
            result.append(element)

    result.sort()
    return result

def symmetrical(set_a, set_b):
    concat = set_a + set_b
    result = []

    for element in concat:
        if (element in set_a and element not in set_b) or (element in set_b and element not in set_a):
            if element not in result:
                result.append(element)

    result.sort()
    return result
