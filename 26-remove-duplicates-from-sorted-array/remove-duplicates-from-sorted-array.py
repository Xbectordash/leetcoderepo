class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = set()
        index = 0

        while index < len(nums):
            if nums[index] not in unique_set:
                unique_set.add(nums[index])
                index += 1
            else:
                nums.pop(index)

        return len(nums)

                