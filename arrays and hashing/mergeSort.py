# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left:List[int],right:List[int])-> List[int]:
            sorted_list=[]
            left_index,right_index=0,0
            while left_index < len(left) and right_index < len(right):
                if left[left_index]<right[right_index]:
                    sorted_list.append(left[left_index])
                    left_index+=1
                else:
                    sorted_list.append(right[right_index])
                    right_index+=1
            
            if left_index<len(left):
                sorted_list.extend(left[left_index:])
            if right_index < len(right):
                sorted_list.extend(right[right_index:])
            
            return sorted_list

        def merge_sort(nums:List[int])->List[int]:
            if len(nums)<=1:
                return nums
            
            mid=len(nums)//2
            left_half=merge_sort(nums[:mid])
            right_half=merge_sort(nums[mid:])

            return merge(left_half,right_half)

        return merge_sort(nums)

s=Solution()
print(s.sortArray([9,8,7,99,34,144,1]))        