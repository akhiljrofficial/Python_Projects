"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects
 of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""


class Solution(object):
    def sortColors(self, nums):
        for j in range(0, len(nums) - 1):
            for i in range(0, len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    self.temp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = self.temp
        return nums


c = Solution()
print(c.sortColors([1, 2, 0, 0, 2, 1]))
