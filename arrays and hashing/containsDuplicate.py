# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_numbers=sorted(nums)
        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i] == sorted_numbers[i + 1]:
                return True
        if len(sorted_numbers) > 1 and sorted_numbers[-2] == sorted_numbers[-1]:
            return True
        return False
