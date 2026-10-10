class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for s in strs:
            k=''.join(sorted(s))
            if k not in groups:
                groups[k]=[]
            groups[k].append(s)
        return list(groups.values())
