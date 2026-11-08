class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:

            if stack and len(stack) >= k-1 : 
                valid = True
                for i in range(k-1) : 
                    if stack[-i -1] != c : 
                        valid = False
                        stack.append(c)
                        break
                if valid : 
                    for i in range(k-1) :
                        stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
