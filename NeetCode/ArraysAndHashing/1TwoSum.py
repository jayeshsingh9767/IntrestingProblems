
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ### Sort the array and use Two Pointer target search.

        nums.sort()
        print(nums)
        start = 0
        end = len(nums) - 1
        while end > start:
            if (nums[start] + nums[end]) > target:
                end -= 1
            elif (nums[start] + nums[end]) < target:
                start += 1
            else:
                return [nums.index(nums[start]), nums.index(nums[end])]
