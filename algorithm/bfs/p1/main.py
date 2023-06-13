# bfs

from collections import deque

visited = [False for i in range(8)]

graph = [
    [],
    [2, 3],
    [1, 3, 4, 5],
    [1, 2, 6, 7],
    [2, 5],
    [2, 4],
    [3, 7],
    [3, 6]
]


def bfs(graph, visited, start):
    q = deque([start])
    visited[start] = True

    while len(q) != 0:
        current_node = q.popleft()
        print(current_node)

        for next_node in graph[current_node]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True


bfs(graph, visited, 1)
