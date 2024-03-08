class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        s = 0
        e = n-1

        while s < e:
            mid = s + (e-s)//2
            if arr[mid] < arr[mid+1]:
                s = mid +1
            else:
                e = mid
            mid = s + (e-s)//2 
        return s
        
        