def quick_sort(data: list) -> list:

    if len(data) < 2:
        return data
    pivot = data.pop()  # Use the last element as the first pivot
    greater: list[int] = []  # All elements greater than pivot
    lesser: list[int] = []  # All elements less than or equal to pivot
    for element in data:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
