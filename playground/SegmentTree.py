"""
@title:      线段树
@difficulty: 中等
@importance: 5/5
@tags:       SegmentTree, 线段树
"""

"""
线段树

当我们需要对数组区间进行修改，查询操作时，可以使用线段树。
                1-8
        1-4             5-8
    1-2   3-4       5-6    7-8
 1-1 2-2 3-3 4-4....     
"""


class SegmentTree:
    def __init__(self, array):
        n = len(array)
        self.array = array
        self.tree = [0] * (2 << n.bit_length())  # 初始化线段树数组
        self.build(0, 0, n - 1, array)  # 构建线段树

    def build(self, node, left, right, array):
        if left == right:  # 叶子节点
            self.tree[node] = array[left]
        else:
            mid = (left + right) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(left_child, left, mid, array)
            self.build(right_child, mid + 1, right, array)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, node, start, end, idx, val):
        if start == end:  # 更新叶子节点
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self.update(left_child, start, mid, idx, val)
            else:
                self.update(right_child, mid + 1, end, idx, val)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, node, start, end, l, r):
        if r < start or end < l:  # 查询范围与当前节点范围无交集
            return 0
        if l <= start and end <= r:  # 当前节点范围完全在查询范围内
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        sum_left = self.query(left_child, start, mid, l, r)
        sum_right = self.query(right_child, mid + 1, end, l, r)
        return sum_left + sum_right


# 使用示例
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)

    print("Sum of values in given range = ",
          st.query(0, 0, st.n - 1, 1, 3))  # 应输出 15
    st.update(0, 0, st.n - 1, 1, 10)  # 更新索引1处的值为10
    print("Updated sum of values in given range = ",
          st.query(0, 0, st.n - 1, 1, 3))  # 应输出 22
