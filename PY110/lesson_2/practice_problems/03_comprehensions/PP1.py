# Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

# total = 0
# for data in munsters.values():
#     if data["gender"] == "male":
#         total += data["age"]

# print(total)

male_age = [data["age"] for data in munsters.values() if data["gender"] == "male"]

print(sum(male_age))
