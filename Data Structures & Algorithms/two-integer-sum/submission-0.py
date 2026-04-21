class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(0, len(nums)):
            for k in range(0, len(nums)):
                if j != k:
                    if nums[j] + nums[k] == target:
                        return [j, k]
        