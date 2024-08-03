class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = []
        for i in range(numRows):
            res.append([])
        mod = numRows - 1
        for cnt, c in enumerate(s):
            if (cnt // mod) % 2 == 0:
                row = cnt % mod
            else:
                row = mod - (cnt%mod)
            res[row].append(c)
        joined = ["".join(row) for row in res]
        return "".join(joined)

s = Solution()
print(s.convert("PAYPALISHIRING", 4))