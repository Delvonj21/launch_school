def interleave(list1, list2):
    new_list = []
    for index in range(len(list1)):
        new_list.extend([list1[index], list2[index]])

    return new_list


list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)  # True