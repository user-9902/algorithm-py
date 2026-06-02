"""
1953. 你可以工作的最大周数
difficulty: middle
importance: 3/5
tags:       math
"""

from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        max_el = max(milestones)
        rest = sum(milestones) - max_el

        return rest * 2 + 1 if max_el > rest + 1 else max_el + rest
