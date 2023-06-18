# baekjoon 1260
from collections import deque

graph = []
visited = []
total_node, total_edge, start_node = map(int, input().split())


def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for n in graph[n]:
        if not visited[n]:
            dfs(n)


def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = True

    while q:
        n = q.popleft()
        print(n, end=' ')

        for n in graph[n]:
            if not visited[n]:
                visited[n] = True
                q.append(n)


for node in range(total_node + 1):
    graph.append([])
    visited.append(False)

for edge in range(total_edge):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(total_node + 1):
    graph[i].sort()

dfs(start_node)
print()

visited = [False for node in range(total_node + 1)]
bfs(start_node)
print()
