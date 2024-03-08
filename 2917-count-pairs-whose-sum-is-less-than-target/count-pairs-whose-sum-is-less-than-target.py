class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l = len(nums)
        count = 0    
        for n in range(l):
            for s in range(n+1,l):
                if nums[n]+nums[s] <target:
                    count+=1
        return count       
        