class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst=[]
        n=len(strs)
        for s in strs:
            freq={}
            for l in s:
                freq[l]=freq.get(l,0)+1
            lst.append(freq)
        visited=[0]*n
        ans=[]
        for i in range(n):
            if visited[i]:
                continue
            temp=[]
            temp.append(strs[i])
            for j in range(i+1,n):
                if lst[i]==lst[j]:
                    visited[j]=1
                    temp.append(strs[j])
            ans.append(temp)
        return ans


        
        