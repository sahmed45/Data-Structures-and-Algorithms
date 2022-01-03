def binary_search(data: list[int], item: int) -> int | None: #data must be sorted

    left = 0
    right = len(data) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = data[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None
