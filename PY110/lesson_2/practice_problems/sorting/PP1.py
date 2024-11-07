# 1  Sort the following list of numbers first in ascending numeric order, then in descending numeric order. Do not mutate the list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

ascending_list = sorted(lst)
print(ascending_list)

descending_list = sorted(lst, reverse=True)
print(descending_list)
