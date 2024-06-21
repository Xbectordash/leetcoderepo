class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        sorted_dict = {key: value for key, value in sorted(count.items(), key=lambda item: item[1])}
        return list(sorted_dict.keys())[-1]
        