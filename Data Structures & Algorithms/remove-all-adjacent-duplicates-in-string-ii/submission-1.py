class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1][0] == c and stack[-1][1] == k-1:
                stack.pop()
            else:
                if stack and stack[-1][0] == c : 
                    _, count = stack.pop()
                    stack.append([c, count+1])
                else : 
                    stack.append([c, 1])


        return "".join(c * count for c, count in stack)
