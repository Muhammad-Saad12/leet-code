

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}
        for i, n in enumerate(nums):
            diff=target-n
            # print (i, n)
            if diff in prevMap:
                print(prevMap[diff],i)
        
# Test
s = Solution()
print(s.twoSum([2,7,11,15], 26)) # [0, 1]