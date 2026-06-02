"""
@title:      937. 重新排列日志文件
@difficulty: 中等
@importance: 3/5
@tags:       sort
"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        @tags:              自定义排序
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       💲sort api的高级使用
        """
        def trans(log: str) -> tuple:
            a, b = log.split(' ', 1)
            return (1,) if b[0].isdigit() else (0, b, a)

        logs.sort(key=trans)
        return logs
