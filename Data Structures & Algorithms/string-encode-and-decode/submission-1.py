class Solution:

    def encode(self, strs: List[str]) -> str:
        output = str(len(strs)) + "\0"
        for string in strs:
            output += str(len(string)) + "\0" + string
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        n_messeges, string = s.split("\0", 1)
        n_messeges = int(n_messeges)
        for _ in range(n_messeges):
            values = string.split("\0", 1)
            length = values[0]
            if not length:
                continue
            rest = values[1]
            output.append(rest[:int(length)])
            string = rest[int(length):]
        return output

