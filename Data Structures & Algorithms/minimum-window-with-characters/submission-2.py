class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        if n2>n1:
            return ""
        f1 = Counter(s)
        freq_t = Counter(t)
        for k , v in freq_t.items():
            if k not in f1:
                return ""
            elif f1[k] < freq_t[k]:
                return ""
        ans  = s
        ans_len = n1
        win_freq = defaultdict(int)
        need = len(freq_t)
        left = 0
        for right in range(n1):
            win_freq[s[right]]+=1
            if s[right] in freq_t:
                if freq_t[s[right]] == 1:
                    need-=1
                freq_t[s[right]]-=1
            while(need == 0):
                new_len = right-left+1
                if new_len < ans_len:
                    ans = s[left:right+1]
                    ans_len = new_len
                win_freq[s[left]]-=1
                if s[left] in freq_t:
                    freq_t[s[left]]+=1
                    if freq_t[s[left]]>0:
                        need+=1
                left+=1
        return ans




        