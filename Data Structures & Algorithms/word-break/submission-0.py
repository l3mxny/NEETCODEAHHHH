class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_list = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(0,i):
                if s[j:i] in word_list or dp[j] == True:
                    dp[i] = True
        return dp[len(s)]
        