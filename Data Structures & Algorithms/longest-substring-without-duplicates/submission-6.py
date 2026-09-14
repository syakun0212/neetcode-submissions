class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_length = 0 

        from collections import defaultdict
        current_window_unique = defaultdict(int)

        while r < len(s):
            while current_window_unique[s[r]] > 0:
                current_window_unique[s[l]] -= 1
                l += 1 
           
            current_window_unique[s[r]] += 1 
            max_length = max(max_length, r-l+1)
            r += 1 
        
        return max_length 
