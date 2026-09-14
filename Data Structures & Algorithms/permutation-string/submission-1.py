class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        k = len(s1)
        if len(s2) < len(s1):
            return False 

        for i in range(0, len(s2)-k+1):
            win = s2[i:i+k]
            if Counter(win) == Counter(s1):
                return True 
        
        return False 