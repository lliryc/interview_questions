class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.processed(s) == self.processed(t)
    def processed(self, s: str):
        res = ""
        for c in s:
            if c == "#":
                if len(res) > 0:
                    res = res[:-1]
            else:
                res += c
        return res

if __name__ == "__main__":
    s = Solution()
    #print(s.backspaceCompare("ab#c","ad#c") == True)
    #print(s.backspaceCompare("ab##", "c#d#") == True)
    #print(s.backspaceCompare("a##c", "#a#c") == True)
    print(s.backspaceCompare("a#c", "b") == False)

