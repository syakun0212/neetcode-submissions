class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        l = 0

        charSet = {} 

        for r in range(len(s)):
            if s[r] in charSet:
                l = max(l, charSet[s[r]]+1)
            
            charSet[s[r]] = r
            longest = max(longest, r-l+1)

        return longest 
