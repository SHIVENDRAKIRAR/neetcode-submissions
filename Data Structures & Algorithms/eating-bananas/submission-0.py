class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            need = 0
            for p in piles:
                r = p%k
                if r==0:
                    need+=p//k
                else:
                    need+=p//k + 1
            return need<=h
        l , r = 1,max(piles)
        while(l<=r):
            m = (l+r)//2
            if check(m):
                ans = m 
                r = m - 1
            else:
                l = m + 1
        return ans
            