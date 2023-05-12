# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        symbols = {}
        start = -1
        max_len = 0

        for i in range(len(s)):
            start = max(start, symbols.get(s[i], -1))
            symbols[s[i]] = i
            if i - start > max_len:
                max_len = i - start

        return max_len