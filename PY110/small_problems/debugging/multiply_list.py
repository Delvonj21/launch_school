# You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain the bug, and provide a solution.


def multiply_list(lst):
    # new_list = []
    # for item in lst:
    #     new_list.append(item * 2)

    # return new_list

    return [item * 2 for item in lst]


print(multiply_list([1, 2, 3]) == [2, 4, 6])
