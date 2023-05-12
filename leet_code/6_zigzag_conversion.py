# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        if numRows == 3:
            return s[::4] + s[1::2] + s[2::4]

        ans = [''] * numRows
        circle = 2 * numRows - 2
        for i in range(len(s)):
            idx = i % (circle)
            if idx >= numRows:
                idx = circle - idx
            ans[idx] += s[i]
        return ''.join(ans)