def quick_sort(_arr) -> [int]:
    if len(_arr) < 2:
        return _arr
    else:
        pivot = _arr[0]
        less_elements = [element for element in _arr[1:] if element <= pivot]
        greater_elements = [element for element in _arr[1:] if element > pivot]
        return quick_sort(less_elements) + [pivot] + quick_sort(greater_elements)


print(quick_sort([234, 12, 344, 2, 1, 7]))
