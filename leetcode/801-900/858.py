"""
858. 镜面反射
数学建模
将光的运动轨迹分为x轴和y轴
经过t秒后到达接收器，可理解为 Sx * t % p == 0 and Sy * t % p == 0
"""

from math import gcd


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        最小公倍数
        """
        g = gcd(p, q)

        p /= g
        p %= 2

        q /= g
        q %= 2

        return 1 if p == 1 and q == 1 else 0 if p == 1 else 2

    def mirrorReflection2(self, p: int, q: int) -> int:
        """
        模拟光的运动方向
        """
        pass
