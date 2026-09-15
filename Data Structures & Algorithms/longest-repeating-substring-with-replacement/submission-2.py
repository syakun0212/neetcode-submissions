class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        res = 0
        curr_win = collections.defaultdict(int)

        for r in range(len(s)):
            curr_win[s[r]] += 1 

            while (r-l+1) - max(curr_win.values()) > k:
                curr_win[s[l]] -= 1 
                l += 1 
            
            res = max(res, r-l+1)

        return res 
