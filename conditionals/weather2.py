# weather = "sunny"

# if weather == "sunny":
#     print("It's a beautiful day!")

# elif weather == "rainy":
#     print("Grab your umbrella")

# else:
#     print("Let's stay inside")

# Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement.

weather = "sunny"

match weather:
    case "sunny":
        print("It's a beautiful day!")
    case "rainy":
        print("Grab your umbrella")
    case _:
        print("Let's stay inside")
