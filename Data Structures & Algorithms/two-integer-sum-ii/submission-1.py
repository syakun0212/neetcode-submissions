class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i, v in enumerate(numbers):
            diff = target - v 

            l = i+1 
            r = len(numbers)
            while l<r:
                 mid = l + (r-l) // 2 
                 if numbers[mid] > diff:
                    r = mid 
                 elif numbers[mid] < diff:
                    l = mid + 1 
                 else:
                    return [i+1, mid+1]

        return 
                