"""
from segmentTree import SegmentTree

a = list(map(float, input('Массив: ').split()))
l, r = list(map(int, input('Границы: ').split()))
tree = SegmentTree(a)
print('Сумма: ', tree.sum(l, r))

from BFS import bfs

n = int(input('Количество вершин: '))
print('Граф:')
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))
s, f = list(map(int, input('Начальная и конечная точки: ').split()))
path = bfs(g, s, f)
print('Путь:', end=' ')
for i in range(len(path)):
    print(path[i], end=' ')
"""

