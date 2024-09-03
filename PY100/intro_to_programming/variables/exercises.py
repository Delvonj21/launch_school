# Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

index         # idiomatic
CatName       # Non-idiomatic, should not use uppercase letters
lazy_dog      # idiomatic
quick_Fox     # Non-idiomatic, should not use uppercase letters
1stCharacter  # Illegal, starts with a number
operand2      # idiomatic
BIG_NUMBER    # Non-idiomatic, should not use uppercase letters
π             # Non-idiomatic, not an ASCII character

# Classify the following potential function names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

index         # idiomatic
CatName       # Non-idiomatic, should not use uppercase letters
lazy_dog      # idiomatic
quick_Fox     # Non-idiomatic, should not use uppercase letters
1stCharacter  # Illegal, starts with a number
operand2      # idiomatic
BIG_NUMBER    # Non-idiomatic, should not use uppercase letters
π             # Non-idiomatic, not an ASCII character

# Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

index         # Non-idiomatic, should not use lowercase letters
CatName       # Non-idiomatic, should not use lowercase letters
snake_case    # Non-idiomatic, should not use lowercase letters
LAZY_DOG3     # idiomatic
1ST           # illegal, should not start with a digit
operand2      # Non-idiomatic, should not use lowercase letters
BIG_NUMBER    # idiomatic
Π             # Non-idiomatic, not an ASCII character

# Classify the following potential class names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

index         # Non-idiomatic, should not start with a lowercase letter
CatName       # idiomatic
Lazy_Dog      # Non-idiomatic, should not use underscores
1ST           # Illegal, Should not start with a digit
operand2      # Non-idiomatic, should not start with a lowercase letter
BigNumber3    # idiomatic
Πi            # Non-idiomatic, not an ASCII character


# What happens when you run the following code? Why?

# NAME = 'Victor'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

# NAME = 'Nina'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

# The program first greets Victor 3 times. It then greets Nina 3 times. Python doesn't have real constants so there is no way to prevent the reassignment of NAME



# Challenge: This program uses a bit of math. Don't let that scare you away -- try it anyway.

# Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. Create a variable named balance that contains the amount of money you will have after 5 years, then print the result. Use a single expression if you can to set balance to the correct value.

balance = (1000.00 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print(balance)

# Repeat the previous question but, this time, use augmented assignment to compute the final result, one year at a time.

balance = 1000.00
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)


# Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.

obj = 'ABcd'            # Reassignment
obj.upper()             # neither
obj = obj.lower()       # Reassignment
print(len(obj))         # neither
obj = list(obj)         # Reassignment 
obj.pop()               # Mutation
obj[2] = 'X'            # Mutation
obj.sort()              # Mutation
set(obj)                # neither
obj = tuple(obj)        # Reassignment