from random import choice


def quicksort(arr: list[int]):
    if len(arr) < 2:
        return arr

    pivot = choice(arr)
    lesser = [i for i in arr if i < pivot]
    equal = [i for i in arr if i == pivot]
    greater = [i for i in arr if i > pivot]

    return quicksort(lesser) + equal + quicksort(greater)


arr = [81, 39, 5, 5, 43, 7, 62, 19, 26]
print(quicksort(arr))
