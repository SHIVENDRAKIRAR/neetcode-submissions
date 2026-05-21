class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        for num in s:
            x = num
            l=1
            while((x+1) in s):
                l+=1
                x+=1
            ans=max(ans , l)
        return ans
        