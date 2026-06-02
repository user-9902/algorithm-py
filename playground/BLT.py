"""
name:        树状数组BIT
description:    
"""
from typing import List


def lowbit(n: int):
    return n & -n


class BIT:
    def __init__(self, nums: List[int]) -> None:
        pass


BIT([1, 2, 3, 4, 5, 6, 7])

res = lowbit(8)
print(bin(res))
