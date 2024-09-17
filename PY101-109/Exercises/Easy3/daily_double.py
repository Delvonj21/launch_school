# Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.


def crunch(str):
    if not str:
        return ""

    result = [str[0]]

    for idx in range(1, len(str)):
        if str[idx] != str[idx - 1]:
            result.append(str[idx])

    return "".join(result)


# These examples should all print True
print(crunch("ddaaiillyy ddoouubbllee") == "daily double")
print(crunch("4444abcabccba") == "4abcabcba")
print(crunch("ggggggggggggggg") == "g")
print(crunch("abc") == "abc")
print(crunch("a") == "a")
print(crunch("") == "")
