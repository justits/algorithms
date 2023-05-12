# https://leetcode.com/problems/string-to-integer-atoi/description/

INF = 2 ** 31


class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0

        if s[0] == '+' or s[0] == '-' or '0' <= s[0] <= '9':
            end_index = 1
            while end_index < len(s) and '0' <= s[end_index] <= '9':
                end_index += 1

            ans = s[:end_index]
            if end_index == 1 and ans in ['-', '+']:
                return 0
            return min(max(int(ans), -INF), INF - 1)
        return 0
