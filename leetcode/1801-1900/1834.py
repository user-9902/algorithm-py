"""
@title:      1834. 单线程 CPU
@difficulty: 中等
@importance: 5/5
@tags:       sort 优选队列
"""
from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        @tags:              sort 优选队列
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       按照时间线执行任务，优先执行花费小的待执行任务
        """
        n = len(tasks)
        task = list(range(n))
        task.sort(key=lambda i: tasks[i][0])    # 捋齐时间线

        que = []
        time = 0
        i = 0
        ans = []
        for j in range(n):  # 一次执行一个任务
            k = task[j]
            if not que:  # 没有待执行的任务 快进到下个任务 确保能执行任务
                time = max(time, tasks[k][0])
            # 当前时间 能执行的任务 能执行都加入优先队列，按照花费时间的优先级
            while i < n and tasks[task[i]][0] <= time:
                heapq.heappush(que, (tasks[task[i]][1], task[i]))
                i += 1
            cost, idx = heapq.heappop(que)
            time += cost
            ans.append(idx)
        return ans
