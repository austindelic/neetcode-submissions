class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        past = {}
        for num in nums:
            if num in past:
                return True
            else:
                past[num] = True
        return False    
        