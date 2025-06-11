# Flawed implementation
"""
Problem Case 1: Non-consecutive duplicates
    items = [2, 1, 2, 3, 2, 4]
    sliced = items[2:5]

Problem Case 2: When the slice doesn't contain the first duplicate
    items = [5, 2, 1, 2, 3, 4]
    sliced = items[3:5]
"""


def inverse_slice1(items: list[int | str], start: int, stop: int) -> list[int | str]:
    sliced = items[start:stop]
    for number in sliced:
        items.remove(number)
    return items


# Proper implementation
def inverse_slice2(items: list[int | str], start: int, stop: int) -> list[int | str]:
    return items[:start] + items[stop:]


if __name__ == "__main__":
    items1 = [12, 14, 63, 72, 55, 24]
    items2 = [12, 14, 63, 72, 55, 24]

    result1 = inverse_slice1(items1, 1, 4)
    result2 = inverse_slice2(items2, 1, 4)

    print(f"{result1}\n{result2}")
