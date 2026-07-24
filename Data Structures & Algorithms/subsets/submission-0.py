class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def sub(idx , arr):
            if idx == n:
                tup = tuple(arr)
                ans.append(list(tup))
                return 
            sub(idx+1 , arr)
            arr.append(nums[idx])
            sub(idx+1 , arr)
            arr.pop()
        
        sub(0 , [])

        return ans
        