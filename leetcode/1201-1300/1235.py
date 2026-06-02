"""
@title:      1235. 规划兼职工作
@difficulty: 中等
@importance: 5/5
@tags:       sort dp
"""

from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        @tags:              sort dp 01背包
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       
        """
        n = len(startTime)
        arr = []
        for i in range(n):
            arr.append([startTime[i], endTime[i], profit[i]])
        arr.sort(key=lambda x: x[1])

        f = [0] * n
        f[0] = arr[0][2]
        for i in range(1, n):
            for j in range(i):
                f[i] = max(f[i], f[j] + arr[i][2] if arr[i]
                           [0] >= arr[j][1] else f[j], arr[i][2])
        return f[n-1]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        @tags:              sort dp
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       
        """
        n = len(startTime)
        arr = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        arr.insert(0, [0, 0, 0])

        n = len(arr)
        f = [0] * n
        for i in range(1, n):
            l = 0
            r = i
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][1] > arr[i][0]:
                    r = mid - 1     # [l, mid-1]
                else:
                    l = mid + 1     # [mid+1, r]
                    # 不选      选
            f[i] = max(f[i-1], f[r] + arr[i][2])
        return f[n-1]


Solution().jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4])
