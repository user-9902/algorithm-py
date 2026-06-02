"""
@title:      225. 用队列实现栈
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""

from collections import deque


class MyStack:
    def __init__(self):
        # in
        self.a = deque()
        # out
        self.b = deque()

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        n = len(self.a)
        for _ in range(n - 1):
            self.b.append(self.a.popleft())

        res = self.a.popleft()
        self.a, self.b = self.b, self.a
        return res

    def top(self) -> int:
        n = len(self.a)
        return self.a[n - 1]

    def empty(self) -> bool:
        return len(self.a) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
stack.pop()
print(stack.a)
