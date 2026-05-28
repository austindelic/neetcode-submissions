class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        closest = r

        while l <= r:
            m = l + ((r - l) // 2)

            ch = 0
            for p in piles:
                ch += math.ceil(p / m)

            if ch <= h:
                closest = m
                r = m - 1
            else:
                l = m + 1

        return closest