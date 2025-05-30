numbers = [1, 2, 3, 4, 5]

# Write two functions to fetch the sixth element from the list: one using the LBYL approach and another using the AFNP approach. In both cases, the function should return None when the element isn't found.


# LBYL
def get_sixth_number():
    if len(numbers) > 5:
        return numbers[5]

    return None


# AFNP
def get_sixth_number():
    try:
        return numbers[5]
    except IndexError:
        return None
