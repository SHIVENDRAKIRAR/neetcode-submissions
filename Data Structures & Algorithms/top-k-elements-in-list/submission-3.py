class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq = Counter(nums)
        arr=[[] for _ in range(n+1)]
        for num , count in freq.items():
            arr[count].append(num)
        ans=[]
        for i in range(n,-1,-1):
            for num in arr[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
        return ans


        
        






            

        