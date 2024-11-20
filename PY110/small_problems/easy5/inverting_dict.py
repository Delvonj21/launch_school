# Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.


def invert_dict(dict):
    return {value: key for key, value in dict.items()}


print(
    invert_dict(
        {
            "apple": "fruit",
            "broccoli": "vegetable",
            "salmon": "fish",
        }
    )
    == {
        "fruit": "apple",
        "vegetable": "broccoli",
        "fish": "salmon",
    }
)  # True