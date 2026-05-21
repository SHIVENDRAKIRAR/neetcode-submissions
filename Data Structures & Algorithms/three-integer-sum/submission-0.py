class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        for i in range(n):
            t  = -nums[i]
            dihh = defaultdict()
            for j in range(i+1,n):
                if nums[j] in dihh:
                 lst = [nums[i] , nums[j] , dihh[nums[j]]]
                 lst.sort()
                 tup = tuple(lst)
                 ans.add(tup)
                dihh[t-nums[j]] = nums[j]
                
        return list(ans)
        