class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        newmap = {}
        for i in nums:
            newmap[i] = newmap.get(i,0) + 1
        ans = min(newmap,key = newmap.get)   
        return ans 

        