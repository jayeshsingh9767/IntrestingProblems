from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ### Pythonic Way using Set
        # num_set = set(nums)
        # if (len(num_set) == len(nums)):
        #     return False
        # else:
        #     return True

        ### -----------------------------------
        ### By Manually creating set
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        return False