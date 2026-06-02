"""
907. 子数组的最小值之和
单调栈
"""


from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.insert(0, -2)
        arr.append(-1)

        stack = []
        ans = 0
        for (right, v) in enumerate(arr):
            if stack:
                while arr[stack[-1]] >= v:
                    left = stack[-2]
                    mid = stack.pop(-1)
                    ans += arr[mid] * (right - mid) * (mid - left)
            stack.append(right)
        return ans


Solution().sumSubarrayMins([3, 1, 2, 4])
