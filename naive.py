class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i : continue
                if nums[i] + nums[j] == target:
                    solution.append(i)
                    solution.append(j)
                    return solution
        return []
