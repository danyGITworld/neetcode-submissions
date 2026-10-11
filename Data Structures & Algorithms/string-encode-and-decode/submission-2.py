class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s += str(len(i)) + "/" + i
        return s
    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            slash = s.find("/", i)
            length = int(s[i:slash])
            l.append(s[slash + 1 : slash + 1 + length])
            i = slash + 1 + length
        return l
        
            
