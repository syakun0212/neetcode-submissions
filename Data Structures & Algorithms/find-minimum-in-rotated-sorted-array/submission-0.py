class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        res = float('inf')
        while l < r:
            if nums[r-1] >=  nums[l]:
                res = min(res, nums[l])
                break

            mid = l + (r-l) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[l]: 
                r = mid 
            else: 
                l = mid + 1
            
        return res