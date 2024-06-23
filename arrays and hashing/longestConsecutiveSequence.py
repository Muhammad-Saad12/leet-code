# 128. Longest Consecutive Sequence
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet=set(nums)  #convert to set
        longestStreak=0      #maintain the longest sequence
        for num in nums:
            if num-1 not in numberSet:   #to check if the current number is the start of the sequence
                length=0
                while (num+length) in numberSet: #to check the length of the sequence if the next number is present in the set
                    length+=1
                longestStreak=max(longestStreak,length) #to update the longest sequence
        return longestStreak
        
s=Solution()
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))

#Solution explanation
# 1. Convert the list to a set to reduce the time complexity of the search operation.
# 2. Initialize the longestStreak to 0.
# 3. Iterate through the list of numbers.
# 4. Check if the current number is the start of the sequence by checking if the number-1 is not in the set.
# 5. If the current number is the start of the sequence, initialize the length of the sequence to 0.
# 6. While the next number is present in the set, increment the length of the sequence.
# 7. Update the longestStreak with the maximum of the current longestStreak and the length of the sequence.
# 8. Return the longestStreak.
# 9. The time complexity of this solution is O(n) as we are iterating through the list of numbers only once.
