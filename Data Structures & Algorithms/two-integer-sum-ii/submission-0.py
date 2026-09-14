class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = collections.defaultdict(int) 
        for i, v in enumerate(numbers):
            diff = target - v 
            if diff in seen: 
                return([seen[diff]+1, i+1])
            seen[v] = i 

        return []  
        