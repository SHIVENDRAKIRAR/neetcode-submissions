class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment={}
        for i in range(len(nums)):
            if nums[i] in compliment:
                return [compliment[nums[i]] ,i]
            compliment[target-nums[i]] = i
        
        