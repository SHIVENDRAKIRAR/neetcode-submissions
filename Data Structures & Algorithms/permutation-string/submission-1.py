class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        f1 = Counter(s1)
        f2 = Counter(s2[:n1])
        for i in range(n1,n2):
            if f1==f2:
                return True
            f2[s2[i]] = f2.get(s2[i] , 0) + 1
            if f2[s2[i-n1]] > 1:
                f2[s2[i-n1]] -=1
            else:
                del f2[s2[i-n1]]
        if f1==f2:
            return True
        return False


        