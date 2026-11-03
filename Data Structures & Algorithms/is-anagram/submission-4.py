class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = {}
        c2 = {}
        if(len(s) != len(t)):
            return False
        for x in s:
            c1[x] = c1.get(x,0) + 1
        for x in t:
            c2[x] = c2.get(x,0) + 1
        return c1 == c2