# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.


def compute_sum(target_num):
    return sum(range(1, target_num + 1))


def compute_product(target_num):
    result = 1
    for num in range(1, target_num + 1):
        result *= num
    return result


prompt1 = "Please enter an integer greater than 0: "
prompt2 = 'Enter "s" to compute the sum, ' 'or "p" to compute the product: '

number = int(input(prompt1))
operation = input(prompt2)
print()

if operation == "s":
    print(
        "The sum of the integers between 1 and " f"{number} is {compute_sum(number)}."
    )
elif operation == "p":
    print(
        "The product of the integers between 1 and "
        f"{number} is {compute_product(number)}."
    )
else:
    print("Oops. Unknown operation.")
