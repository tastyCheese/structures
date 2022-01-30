class SegmentTree(object):

    def __init__(self, source_list):
        self.__length = len(source_list)
        self.__tree = [0 for _ in range(self.__length << 2)]
        self.__build(source_list, 1, 0, self.__length - 1)

    def __build(self, source_list, vertex, left, right):
        if left == right:
            self.__tree[vertex] = source_list[left]
        else:
            middle = (left + right) >> 1
            self.__build(source_list, vertex << 1, left, middle)
            self.__build(source_list, (vertex << 1) + 1, middle + 1, right)
            self.__tree[vertex] = self.__tree[vertex << 1] + self.__tree[(vertex << 1) + 1]

    def __sum(self, vertex, left, right, cur_left, cur_right):
        if cur_left > cur_right:
            return 0
        elif (left == cur_left) and (right == cur_right):
            return self.__tree[vertex]
        middle = (left + right) >> 1
        return self.__sum(vertex << 1, left, middle, cur_left, min(cur_right, middle)) \
            + self.__sum((vertex << 1) + 1, middle + 1, right, max(cur_left, middle + 1), cur_right)

    def __update(self, vertex, left, right, upd_vertex, new_value):
        if left == right:
            self.__tree[vertex] = new_value
        else:
            middle = (left + right) >> 1
            if upd_vertex <= middle:
                self.__update(vertex << 1, left, middle, upd_vertex, new_value)
            else:
                self.__update((vertex << 1) + 1, middle + 1, right, upd_vertex, new_value)
            self.__tree[vertex] = self.__tree[vertex << 1] + self.__tree[(vertex << 1) + 1]

    def sum(self, left, right):
        return self.__sum(1, 0, self.__length - 1, left, right)

    def update(self, upd_vertex, new_value):
        self.__update(1, 0, self.__length - 1, upd_vertex, new_value)
