# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height):
        n = len(height)
        left = 0
        right = n - 1
        most_water = 0
        while left < right:
            current_height = min(height[left], height[right])
            most_water = max(most_water, (right - left) * current_height)
            if height[left] > height[right]:
                right -= 1
                while height[right] < current_height:
                    right -= 1
            else:
                left += 1
                while height[left] < current_height:
                    left += 1

        return most_water
