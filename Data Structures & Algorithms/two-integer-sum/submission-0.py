class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {} # value:index

        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in have:
                return [have[diff], j]
            have[nums[j]] = j
        return 

         