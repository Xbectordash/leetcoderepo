class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in num_dic:
                return [num_dic[compliment],i]
            num_dic[num] = i
        return []        
        
        