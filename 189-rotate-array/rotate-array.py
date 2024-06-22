class Solution:
    def reverse(self,s, l, nums):
        while s < l:
            nums[s], nums[l] = nums[l], nums[s]
            s += 1
            l -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        k %=len(nums)
        n = len(nums)
        self.reverse(0,len(nums)-1,nums)  
        self.reverse(0,k-1,nums)
        self.reverse(k,n-1,nums)
        
                