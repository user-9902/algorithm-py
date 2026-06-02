"""
@title:      HJ24 合唱队
@difficulty: 中等
@importance: 5/5
@tags:       LIS最长递增子序列  💲经典题型的变体。
"""
import bisect

n = int(input())
height = [int(i) for i in input().split()]


def LIS(arr):
    # LIS最长递增子序列
    n = len(arr)
    ans = [arr[0]]
    f = [0] * n
    for i in range(1, n):
        if arr[i] > ans[-1]:
            ans.append(arr[i])
            f[i] = len(ans)
        else:
            r = bisect.bisect_left(ans, arr[i])
            ans[r] = arr[i]
            f[i] = r + 1
    return f


l = LIS(height)  # l[i]表示为：以第 i 个元素为尾巴的最长递增子序列的长度
r = LIS(height[::-1])[::-1]
sums = [l[i] + r[i] - 1 for i in range(n)]
res = n - max(sums)
print(res)
