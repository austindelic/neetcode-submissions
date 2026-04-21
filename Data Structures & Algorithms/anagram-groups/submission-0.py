from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        counters = []
        for string in strs:
            added = False
            this_counter = Counter(string)
            for i, n in enumerate(counters):
                if this_counter == n:
                    output[i].append(string)
                    added = True
            if not added:
                output.append([string])
                counters.append(this_counter)
        return output

                
                



        