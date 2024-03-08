class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = []
        for i in range(l):
            nums.append(nums[i])
        return nums

        