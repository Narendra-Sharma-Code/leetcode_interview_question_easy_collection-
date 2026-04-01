from typing import List
nums = [1,2,3,4,1]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
    
print(Solution().containsDuplicate(nums))