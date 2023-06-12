# dfs

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


def dfs(graph, visited, start):
    if visited[start]:
        return
    visited[start] = True
    print(start)
    for next_node in graph[start]:
        dfs(graph, visited, next_node)


dfs(graph, visited, 1)
