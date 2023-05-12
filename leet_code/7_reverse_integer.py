# https://leetcode.com/problems/reverse-integer/

INF = 2 ** 31


class Solution:
    def reverse(self, x):
        pos = x >= 0
        x *= -1 if x < 0 else 1
        ans = int(str(x)[::-1])
        if ans > INF - pos:
            return 0
        return ans if pos else -ans
