class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group={}
        for i in nums:
            group[i]=group.get(i,0)+1
        final=[]
        j=0
        while j<k:
            m=0
            z=0
            for i in group:
                if group.get(i)>m:
                    m=group.get(i)
                    z=i
            final.append(z)
            del group[z]
            j+=1
        return final




