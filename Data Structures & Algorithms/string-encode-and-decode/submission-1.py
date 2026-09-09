class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for x in strs: 
            res += (str(len(x)) + "#" + x)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        num = ""
        i = 0
        # print("len: ", len(s))
        while i < len(s):
            if s[i] == "#":
                word = s[i + 1:i + 1 + int(num)]
                res.append(word)
                i = i + 1 + int(num)
                num = ""
            if i < len(s):
                num += s[i]
                i += 1        
        return res
