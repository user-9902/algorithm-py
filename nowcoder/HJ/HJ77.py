"""
@title:      HJ77 火车进站
@difficulty: 中等
@importance: 5/5
@tags:       回溯 栈
"""

n = int(input())
arr = input().split()

ans = []
stack = []
cur = []


def dfs(i):
    if len(cur) + len(stack) == n:
        ans.append(cur[:] + stack[::-1])
        return
    if i == n:
        return
    # 先将所有的元素压入栈中
    stack.append(arr[i])
    dfs(i + 1)
    stack.pop()  # 回溯

    # 选择从 stack 中弹出一个元素
    if stack:
        cur.append(stack.pop())
        dfs(i)
        stack.append(cur.pop())  # 回溯


dfs(0)
ans.sort()
for i in ans:
    print(" ".join(i))
