from collections import Counter

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for h in range(max(height), 0, -1):
            indices = [i for i, x in enumerate(height) if x >= h]
            if len(indices) < 2:
                continue
            for i in range(len(indices) - 1):
                total += (indices[i + 1] - indices[i] -1)
        return total
        