def bfs(graph: list, start: int, finish: int) -> list:
    n = len(graph)
    queue = [start]
    used = [False for _ in range(n)]
    dist = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    used[start] = True

    while len(queue) > 0:
        vertex = queue.pop(0)
        for i in range(len(graph[vertex])):
            u = graph[vertex][i]
            if not used[u]:
                used[u] = True
                queue.append(u)
                dist[u] = dist[vertex] + 1
                parent[u] = vertex

    if used[finish]:
        path = []
        v = finish
        while v != -1:
            path.append(v)
            v = parent[v]
        path.reverse()
        return path
    else:
        print('Нет пути.')
        return []
