class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                if i < hashmap[diff]:
                    return [i, hashmap[diff]]
                else:
                    return [hashmap[diff], i]
            else:
                hashmap[n] = i



        