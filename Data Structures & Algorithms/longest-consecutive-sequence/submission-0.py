class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        numSet = set(nums)

        for i in numSet:
            if (i-1) not in numSet:
                #means this can be a starting point 
                length = 0 
                while (i+length) in numSet:
                    length += 1 
                longest = max(longest, length)

        return longest 