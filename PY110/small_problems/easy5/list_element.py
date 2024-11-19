# Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.


def multiply_items(list_a, list_b):
    # result = []

    # for item in range(len(list_a)):
    #     result.append(list_a[item] * list_b[item])

    # return result

    return [num1 * num2 for num1, num2 in zip(list_a, list_b)]


list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18])  # True
