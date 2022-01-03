def merge_sort(data: list) -> list:


    def merge(left: list, right: list) -> list:

        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(data) <= 1:
        return data
    mid = len(data) // 2
    return merge(merge_sort(data[:mid]), merge_sort(data[mid:]))
