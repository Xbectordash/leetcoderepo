class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        current_len = 0
        for i in nums:
            if i == 1:
                current_len += 1
                max_len = max(current_len,max_len)
            else:
                current_len = 0
        return max_len            
        
            
        return max_len    

        