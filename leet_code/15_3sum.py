# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_el = nums[i] + nums[j] + nums[k]
                if sum_el == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum_el > 0:
                    k -= 1
                else:
                    j += 1
        return ans