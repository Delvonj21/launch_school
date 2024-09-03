# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

bill_amount = float(input("What is the bill? "))
tip_rate = float(input("What is the tip percentage? "))

tip = bill_amount * (tip_rate // 100)
total = tip + bill_amount

print(f"The tip is ${tip:.2f}")
print(f"The total is ${total:.2f}")
