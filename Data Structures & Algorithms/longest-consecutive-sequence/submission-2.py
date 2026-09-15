class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = set(nums)
        longest = 0 

        for i in unique:
            if (i-1) not in unique: # startig numbers 
                length = 0 
                while (i+length) in unique:
                    length += 1 
                longest = max(longest,length)

        return longest 