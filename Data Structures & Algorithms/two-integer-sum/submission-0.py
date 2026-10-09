class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[0,0]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i]+nums[j]==target and i!=j):
                    a[0]=i
                    a[1]=j
                    return a
