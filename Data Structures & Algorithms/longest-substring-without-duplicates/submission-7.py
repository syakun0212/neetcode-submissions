class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = {} 
        l = 0 
        maxLength = 0 

        for r in range(len(s)):
            if s[r] in charSet:
                l = max(charSet[s[r]]+1, l)
            charSet[s[r]] = r 
            maxLength = max(maxLength, r-l+1)

        return maxLength
            