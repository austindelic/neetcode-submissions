class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getCount(s: str):
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            return count
        output = []
        prev_count = {}
        length = 0
        for s in strs:
            count = getCount(s)
            key = tuple(count)
            if key in prev_count:
                index = prev_count[key]
                output[index].append(s)
            else:
                prev_count[key] = length
                output.append([s])
                length += 1
        return output

