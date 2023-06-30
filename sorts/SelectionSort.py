def find_smallest(_arr):
    smallest = _arr[0]
    smallest_index = 0
    for i in range(1, len(_arr)):
        if _arr[i] < smallest:
            smallest = _arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(_arr):
    new_arr = []
    for i in range(len(_arr)):
        smallest = find_smallest(_arr)
        new_arr.append(_arr.pop(smallest))
    return new_arr


print(selection_sort([5, 3, 34, 10, 51]))
