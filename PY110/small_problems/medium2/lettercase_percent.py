def percentage(count, total_count):
    return f"{(count / total_count) * 100:.2f}"


def letter_percentages(string):
    total_chars = len(string)
    upper_count = 0
    lower_count = 0
    neither_count = 0

    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        else:
            neither_count += 1

    return {
        "lowercase": percentage(lower_count, total_chars),
        "uppercase": percentage(upper_count, total_chars),
        "neither": percentage(neither_count, total_chars),
    }


expected_result = {
    "lowercase": "50.00",
    "uppercase": "10.00",
    "neither": "40.00",
}
print(letter_percentages("abCdef 123") == expected_result)

expected_result = {
    "lowercase": "37.50",
    "uppercase": "37.50",
    "neither": "25.00",
}
print(letter_percentages("AbCd +Ef") == expected_result)

expected_result = {
    "lowercase": "0.00",
    "uppercase": "0.00",
    "neither": "100.00",
}
print(letter_percentages("123") == expected_result)
