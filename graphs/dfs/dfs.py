from collections import deque

with open('input.txt', mode='r') as file:
    data = [line.strip() for line in file.readlines()]
    N = int(data[0])
    graph = {}
    for index, number in enumerate(data[1:-1]):
        temp = []
        for ji, j in enumerate(list(map(int, number.split()))):
            if j != 0:
                temp.append(ji + 1)
        graph[index + 1] = temp
    start_node = int(data[-1].split()[0])
    end_node = int(data[-1].split()[1])


def dfs(node, search_request, _graph, visited=[]):
    print(graph)
    if node == search_request:
        return True
    if node in visited:
        return False

    visited.append(node)
    for neighbor_node in _graph[node]:
        if neighbor_node not in visited:
            reached = dfs(neighbor_node, search_request, _graph, visited)
            if reached:
                return True
    return False


result = dfs(start_node, end_node, graph)

with open('output.txt', mode='w') as file:
    file.write(str(result))
