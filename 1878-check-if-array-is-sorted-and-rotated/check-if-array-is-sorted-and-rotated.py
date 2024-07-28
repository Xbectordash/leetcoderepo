class Solution:
    def check(self, nums: List[int]) -> bool:

        rotation = 1

        for i in range(1,len(nums)):
            if nums[i] < nums[i - 1]:
                if rotation < 1:   
                    return False
                rotation -= 1 
        if nums[-1] > nums[0] and rotation == 0:
            return False              
            
        return True        

        
        