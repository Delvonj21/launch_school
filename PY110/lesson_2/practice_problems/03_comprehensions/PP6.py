# Given the following data structure, return a new list identical in structure to the original but, with each number incremented by 1. Do not modify the original data structure. Use a comprehension.

lst = [{"a": 1}, {"b": 2, "c": 3}, {"d": 4, "e": 5, "f": 6}]


def increment_value(dict):
    value_dict = {key: value + 1 for key, value in dict.items()}
    return value_dict


value_list = [increment_value(value) for value in lst]
print(value_list)
