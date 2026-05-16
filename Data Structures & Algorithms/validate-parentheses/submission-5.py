class Solution:
    def isValid(self, s: str) -> bool:
        open_b = "[{("
        b = [] #stack
        for c in s:

            if c in open_b:
                b.append(c)
            else:
                if len(b) == 0:
                    return False
                if c == "}" and b.pop() != "{":
                    return False
                elif c == "]" and b.pop() != "[":
                    return False
                elif c == ")" and b.pop() != "(":
                    return False
                else:
                    continue
        if b:
            return False
        else:
            return True



        