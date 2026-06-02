class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n >= 2 and n % 2 == 0:
            n //= 2
        return n == 1
