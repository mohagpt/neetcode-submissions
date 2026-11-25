from collections import defaultdict
import heapq

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}                                # word -> longest chain ending at word
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                shorter = word[:i] + word[i + 1:]      # remove one letter
                if shorter in dp:
                    dp[word] = max(dp[word], dp[shorter] + 1)
        return max(dp.values(), default=0)