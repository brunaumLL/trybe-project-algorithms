def sorted_string(string):
    n = len(string)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if string[i] < string[min_index]:
                min_index = i
        if string[j] > string[min_index]:
            aux = string[j]
            string[j] = string[min_index]
            string[min_index] = aux
    sorted_string = "".join(string)
    return sorted_string


def is_anagram(first_string, second_string):
    first_lower = [letter.lower() for letter in first_string]
    second_lower = [letter.lower() for letter in second_string]

    sorted_first = sorted_string(first_lower)
    sorted_second = sorted_string(second_lower)

    if first_string == "" or second_string == "":
        return (sorted_first, sorted_second, False)
    if len(first_lower) != len(second_lower):
        return (sorted_first, sorted_second, False)
    if sorted_first != sorted_second:
        return (sorted_first, sorted_second, False)

    return (sorted_first, sorted_second, True)
