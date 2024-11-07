# 3 Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort(key=str)
print(lst)

lst.sort(reverse=True, key=str)
print(lst)
