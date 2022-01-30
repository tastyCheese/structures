"""
from segmentTree import SegmentTree

a = list(map(float, input('Массив: ').split()))
l, r = list(map(int, input('Границы: ').split()))
tree = SegmentTree(a)
print('Сумма: ', tree.sum(l, r))

"""
from dijkstra import dijkstra

n = int(input('Количество вершин: '))
g = []
for i in range(n):
    e = int(input('Количество рёбер вершины ' + str(i) + ': '))
    edges = []
    print('Рёбра и веса:')
    for _ in range(e):
        edges.append(list(map(int, input().split())))
    g.append(edges)
s, f = list(map(int, input('Начальная и конечная точки: ').split()))
path = dijkstra(g, s, f)
print('Расстояние:', path[0])
print('Путь:', end=' ')
for i in range(len(path[1])):
    print(path[1][i], end=' ')


