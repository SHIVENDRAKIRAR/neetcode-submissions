class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        f = defaultdict(int)
        n = len(s)
        i , j = 0 , 0
        ans = 0
        while(j<n):
            f[s[j]]+=1
            while(f[s[j]]>1):
                f[s[i]]-=1
                i+=1
            ans = max(ans , j-i+1)
            j+=1  
        return ans   