class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        z=nums.count(0)
        pro=1
        res=[0]*n

        for num in nums:
            if num==0:
                continue
            pro = pro*num

        if z>1:
            return res

        elif z==1:
            idx=nums.index(0)
            res[idx]=pro
            return res
            
        else:
            for i in range(n):
                res[i]=int(pro/nums[i])
            return res

        