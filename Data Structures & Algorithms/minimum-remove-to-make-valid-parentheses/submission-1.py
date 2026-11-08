class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removed = set()
        for i, c in enumerate(s) : 
            if c == "(" : 
                stack.append(i)
            elif c == ")" : 
                if not stack : 
                    removed.add(i)
                else : 
                    stack.pop()

        while stack : 
            removed.add(stack.pop())
        res = []
        for i, c in enumerate(s):
            if i not in removed:
                res.append(c)
        return "".join(res)