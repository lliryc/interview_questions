class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # for empty strings
        
        # patterns starting with '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        
        return dp[m][n]

# Tests:
solution = Solution()
print(solution.isMatch("aa", "a"))      # False
print(solution.isMatch("aa", "*"))      # True
print(solution.isMatch("cb", "?a"))     # False
print(solution.isMatch("adceb", "*a*b")) # True
print(solution.isMatch("acdcb", "a*c?b")) # False
