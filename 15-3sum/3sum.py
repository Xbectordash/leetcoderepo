class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        result = []
        for i in range(len(num)):
            if i > 0 and num[i] == num[i -1]:
                continue
            target = - num[i]
            l = i + 1
            r = len(num) - 1
            while l < r:                    
                sums = num[l] + num[r]
                if sums == target:
                    result.append([num[i],num[l],num[r]])

                    l += 1
                    r -= 1

                    while l < r and num[l] == num[l-1]:
                        l += 1
                    while l < r and num[r] == num[r+1]:
                        r -= 1    
                elif sums < target:
                    l += 1
                else:
                    r -= 1        
        return result            

        