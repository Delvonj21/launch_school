# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

length = float(input("Enter the length of room in meters: "))
width = float(input("Enter width of room in meters: "))

square_meter = length * width
square_feet = 10.7639 * square_meter

print(f"The area of the room is: {square_feet:.2f} square feet")
print(f"The area of the room is: {square_meter:.2f} square meters")
