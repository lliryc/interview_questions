class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena = len(a)
        lenb = len(b)
        maxlen = max(lena, lenb)
        minlen = min(lena, lenb)
        maxstr = a[::-1] if lena == maxlen else b[::-1]
        minstr = b[::-1] if lenb == minlen else a[::-1]
        res = [0] * (maxlen+1)
        shift = 0
        for i in range(maxlen):
            if i >= minlen:
                sum = ord(maxstr[i]) - ord('0') + shift
            else:
                sum = ord(maxstr[i]) + ord(minstr[i]) - 2*ord('0') + shift
            res[i] =  int(sum%2)
            shift = sum // 2
        res[-1] = shift
        if res[-1] == 0:
            res.pop()
        return str.join("",[chr(res[i] + ord('0')) for i in range(len(res)-1, -1, -1)])

s = Solution()
#print(s.addBinary("1010", "1011"))
#print(s.addBinary("11","1"))
print(s.addBinary("1111", "1111"))
