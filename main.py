from segmentTree import SegmentTree

a = list(map(int, input('Массив: ').split()))
l, r = list(map(int, input('Границы: ').split()))
tree = SegmentTree(a)
print('Сумма: ', tree.sum(l, r))
