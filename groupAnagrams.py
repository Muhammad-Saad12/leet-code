# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        return list(anagrams.values())
                
s = Solution()
print(s.groupAnagrams(["saad","dsaa","cat","eat","feat","tca"]))

# Explanation of Algoirthm
# 1. Empty dictionary is initialized
# 2. For each word in the List create a sorted word i-e cat=act 
# 3. If sorted word is not in anagrams it means its the first time the word is appearning so initialize it with empty list
# 4. If sorted word is already in anagram then it means we have already seen this word and add it to current list