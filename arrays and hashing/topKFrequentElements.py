# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        for num in nums:
            if num not in frequency:
                frequency[num]=[]
            frequency[num].append(num)
        sorted_lists= sorted(frequency.values(),key=len,reverse=True)
        top_k_elements=[list[0] for list in sorted_lists[:k]]    
        return top_k_elements


s=Solution()
print(s.topKFrequent([5,2,3,3,2,3],2))

# Explanation of Algoirthm
# 1. Empty dictionary is initialized
# 2. For each number in a list find if the number is added to dictionary or not
# 3. If its not in the dictionary add it to the new row 
# 4. If its already present in the dictionary then append it to the find number.At this point you will be having a key value pair of the number corresponding to the number how much it appeard. E.g. If 3 appeared 3 times then it will be [3,3,3]
# 5. Now that we have a key value pair in desired format we can sort it in descending order beacuse of the maximum appearance condition
# 6. In the final step I have used list comprehension technique to get the results. List[0] will take the first element of each list. 
# 7. The last step is to slice the result till k and return it