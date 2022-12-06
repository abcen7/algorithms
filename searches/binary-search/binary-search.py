with open('input.txt', mode='r') as file:
    data = [line.strip() for line in file.readlines()]
    array1 = [int(x) for x in data[1].split()]
    array2 = [int(x) for x in data[2].split()]


def binary_search(_array: list, search_item):
    start = 0
    end = len(_array) - 1
    while start <= end:
        middle = (start + end) // 2
        if _array[middle] < search_item:
            start = middle + 1
        elif _array[middle] > search_item:
            end = middle - 1
        else:
            return True
    return False


result = []
for number in array2:
    if binary_search(array1, number):
        result.append("YES")
    else:
        result.append("NO")

with open('output.txt', mode='w') as file:
    file.write("\n".join(result))
