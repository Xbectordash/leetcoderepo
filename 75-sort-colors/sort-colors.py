class Solution:
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2    
        left = self.merge_sort(arr[:mid])
        right= self.merge_sort(arr[mid:])
        return self.merge(left,right)
    def merge(self,left, right):
        result = []
        i,j = 0,0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])    
        return result        



    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = self.merge_sort(nums)
        nums[:] = sorted_nums 
        