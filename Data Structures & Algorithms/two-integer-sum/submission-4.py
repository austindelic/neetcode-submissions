class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, j in enumerate(nums):
            for i2, k in enumerate(nums):
                if i2 != i1 and j + k == target:
                    return [i1, i2]
        