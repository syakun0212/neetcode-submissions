class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict

        d = defaultdict(int)
        for i in nums:
            if i in d:
                return True 
            d[i] += 1 

        return False 