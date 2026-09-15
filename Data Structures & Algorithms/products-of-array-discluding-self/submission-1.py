class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prefix prod 
        prefixProd = [1] * len(nums) 
        prod = 1 
        for i in range(0, len(nums)-1):
            prod *= nums[i]
            prefixProd[i+1] = prod

        # multiply by post fix 
        prod = 1
        for i in range(len(nums)-1,0,-1):
            prod *= nums[i]
            prefixProd[i-1] *= prod 
        
        return prefixProd

