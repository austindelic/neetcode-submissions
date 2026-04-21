class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for num in nums:
            values[num] = 0
        for num in nums:
            if values[num] == None:
                values[num] = 0
            values[num] += 1
        for num in nums:
            if values[num] > 1:
                return True
        else:
            return False
        