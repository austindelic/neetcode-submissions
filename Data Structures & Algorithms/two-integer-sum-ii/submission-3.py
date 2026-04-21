class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, -1
        while l < len(numbers) - abs(r):
            current = numbers[l] + numbers[r]

            if current == target:
                return [l + 1, len(numbers) - abs(r) + 1]
            
            if current < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]