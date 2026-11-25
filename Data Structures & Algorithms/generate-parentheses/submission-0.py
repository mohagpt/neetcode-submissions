class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, current = [], []
        def build(opened, closed):
            if len(current) == 2 * n:
                result.append("".join(current))
                return
            if opened < n:
                current.append("(")
                build(opened + 1, closed)
                current.pop()
            if closed < opened:                # never close more than were opened
                current.append(")")
                build(opened, closed + 1)
                current.pop()
        build(0, 0)
        return result