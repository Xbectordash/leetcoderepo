class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = []
        l = len(nums)
        res = []
        for i in range(l):
            n.append(nums[nums[i]])
        return n    
        