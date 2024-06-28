class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        spos = 0
        tpos = 0
        while spos < len(s):
            if tpos < len(t) and s[spos] == t[tpos]:
                tpos += 1
            spos+=1
        return len(t) - tpos

sol = Solution()
print(sol.appendCharacters("coaching", "coding"))