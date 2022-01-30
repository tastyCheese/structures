from math import inf


def dijkstra(graph: list, start: int, finish: int) -> list:
    n = len(graph)
    dist = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    used = [False for _ in range(n)]
    dist[start] = 0

    for i in range(n):
        vertex = -1
        for j in range(n):
            if (not used[j]) and ((vertex == -1) or (dist[j] < dist[vertex])):
                vertex = j

        if dist[vertex] != inf:
            used[vertex] = True
            for j in range(len(graph[vertex])):
                to = graph[vertex][j][0]
                weight = graph[vertex][j][1]
                if (dist[vertex] + weight) < dist[to]:
                    dist[to] = dist[vertex] + weight
                    parent[to] = vertex
        else:
            print('Несвязный граф!')
            return [inf, []]

    path = []
    v = finish
    while v != start:
        path.append(v)
        v = parent[v]
    path.append(start)
    path.reverse()
    return [dist[finish], path]
