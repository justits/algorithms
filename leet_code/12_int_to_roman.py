# https://leetcode.com/problems/integer-to-roman/

num_to_symbols = {1: 'I',
                  5: 'V',
                  10: 'X',
                  50: 'L',
                  100: 'C',
                  500: 'D',
                  1000: 'M'}


class Solution:
    def intToRoman(self, num):
        ans = ''
        rank = 1000
        while rank >= 1:
            whole = num // rank
            num -= rank * whole
            if whole > 0:
                if num_to_symbols.get(rank * 5):
                    if whole == 4:
                        ans += num_to_symbols[rank] + num_to_symbols[rank * 5]
                    elif whole == 9:
                        ans += num_to_symbols[rank] + num_to_symbols[rank * 10]
                    else:
                        if whole >= 5:
                            ans += num_to_symbols[rank * 5]
                            whole -= 5
                        ans += whole * num_to_symbols[rank]
                else:
                    ans += whole * num_to_symbols[rank]
            rank = rank // 10
        return ans
