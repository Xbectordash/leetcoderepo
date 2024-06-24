class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Calculate prefix products and store in answer array
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Calculate suffix products and update answer array
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

        