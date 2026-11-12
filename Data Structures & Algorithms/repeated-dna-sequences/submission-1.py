class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, repeated = set(), set()
        for i in range(len(s) - 9):          # every start index of a 10-letter window
            subStr = s[i:i + 10]
            if subStr in seen:
                repeated.add(subStr)
            else:
                seen.add(subStr)
        return list(repeated)