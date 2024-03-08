class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = numbers
        t = target
        l,r = 0, len(numbers)-1
        while l < r :
            sum = numbers[l] + numbers[r]
            if sum > t:
                r-= 1
            elif sum < t:
                l += 1
            else:
                return([l+1,r+1])
        return[]        

        