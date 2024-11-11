# Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]


new_list = []

for sublist in lst:
    new_sublist = []
    for number in sublist:
        if number % 3 == 0:
            new_sublist.append(number)

    new_list.append(new_sublist)

print(new_list)
