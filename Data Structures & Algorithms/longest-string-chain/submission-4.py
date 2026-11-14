class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}                                   # dp[w] = longest chain ending at w
        for w in sorted(words, key=len):          # shortest first: predecessors are done before w
            best = 0
            for i in range(len(w)):
                pred = w[:i] + w[i+1:]            # w with the letter at i removed
                best = max(best, dp.get(pred, 0))
            dp[w] = 1 + best
        return max(dp.values())