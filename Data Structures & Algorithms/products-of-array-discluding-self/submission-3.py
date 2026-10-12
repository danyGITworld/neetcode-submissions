class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final=[]
        zeroes=[]
        l=1
        for i,r in enumerate(nums):
            if r!=0:
                l*=r
            else:
                zeroes.append(i)
        for i in range(len(nums)):
            final.append(l)
        if len(zeroes)>1:
            return [0]*len(final)
        if zeroes:
            for i in range(len(nums)):
                if i not in zeroes:
                    final[i]=0
                else:
                    continue
        else:
            for i in range(len(nums)):
                z=final[i]/nums[i]
                final[i]=int(z)
        return final
