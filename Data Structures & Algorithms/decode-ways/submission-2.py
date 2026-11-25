class Solution:
    def numDecodings(self, s: str) -> int:
        prev2, prev1 = 1, 1                    # ways for the prefixes ending 2 and 1 characters back
        for i, ch in enumerate(s):
            ways = 0
            if ch != "0":
                ways += prev1                  # this digit alone
            if i > 0 and 10 <= int(s[i - 1:i + 1]) <= 26:
                ways += prev2                  # this digit together with the previous one
            prev2, prev1 = prev1, ways
        return prev1