class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s : 
            match c :
                case '(' | '[' | '{': 
                    stack.append(c)
                case ')' :
                    if not stack : 
                        return False
                    st = stack.pop()
                    if st != '(' :
                        return False
                case '}' :
                    if not stack : 
                        return False
                    st = stack.pop()
                    if st != '{' :
                        return False
                case ']' :
                    if not stack : 
                        return False
                    st = stack.pop()
                    if st != '[' :
                        return False
                case _ : 
                    return False
        return not stack
                