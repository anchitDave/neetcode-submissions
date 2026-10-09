class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        a = ''
        while i < len(s):
            
            if s[i] == '#':
                l = int(a)
                res.append(s[i+1:i+l+1])
                a = ''
                i += l+1
            else:
                a+=s[i]
                i+=1

        return res
