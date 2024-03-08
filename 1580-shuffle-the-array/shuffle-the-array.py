class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_pointer = 0
        y_pointer = n
        solution = []
        while x_pointer<=n and y_pointer <= len(nums)-1:
            solution.append(nums[x_pointer])
            x_pointer +=1
            solution.append(nums[y_pointer])
            y_pointer += 1
        return solution    

        