# https://leetcode.com/problems/longest-palindromic-substring/
# алгоритм Манакера

class Solution:
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s
        n = len(s)

        d1 = [0] * n
        left, right = 0, -1
        for i in range(n):
            k = 1 if i > right else min(d1[left + right - i], right - i + 1)
            while i + k < n and i - k >= 0 and s[i + k] == s[i - k]:
                k += 1
            d1[i] = k
            if i + k - 1 > right:
                left = i - k + 1
                right = i + k - 1

        d2 = [0] * n
        left, right = 0, -1
        for i in range(n):
            k = 0 if i > right else min(d2[left + right - i + 1], right - i + 1)
            while i + k < n and i - k - 1 >= 0 and s[i + k] == s[i - k - 1]:
                k += 1
            d2[i] = k
            if i + k - 1 > right:
                left = i - k
                right = i + k - 1

        max_palindromic_1 = max(d1)
        max_palindromic_2 = max(d2)
        if max_palindromic_1 > max_palindromic_2:
            index = d1.index(max_palindromic_1)
            return s[index - max_palindromic_1 + 1: index + max_palindromic_1]
        else:
            index = d2.index(max_palindromic_2)
            return s[index - max_palindromic_2: index + max_palindromic_2]
