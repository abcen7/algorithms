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


def bfs(start_point, search_request, _graph):
    search_queue = deque()
    search_queue += _graph[start_point]
    visited = []
    while search_queue:
        node = search_queue.popleft()
        if node not in visited:
            if node == search_request:
                return len(visited)
            else:
                search_queue += _graph[node]
                visited += [node]
    return -1


result = bfs(start_node, end_node, graph)

with open('output.txt', mode='w') as file:
    file.write(str(result))
