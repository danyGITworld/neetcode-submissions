class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0]*26
        b=[0]*26
        for i in s:
            l=ord(i)-97
            a[l]+=1
        for i in t:
            l=ord(i)-97
            b[l]+=1
        for i in range(26):
            if (a[i]!=b[i]):
                return False
        return True