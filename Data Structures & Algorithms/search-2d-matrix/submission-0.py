class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for row in matrix:
            nums += row

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            value = nums[m]
            if value < target:
                l = m + 1
            elif value > target:
                r = m - 1
            else:
                return True
        return False
        