class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        def max_e(arr):
            ma = 0
            for i in arr:
              if i > ma:
                ma = i
            return ma    
        for i in nums:
           dic[i] = dic.get(i,0)+1
        if max_e(dic.values()) > 1:
            return True
        else: return False 
        