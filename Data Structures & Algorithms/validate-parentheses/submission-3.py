class Solution:
    def isValid(self, s: str) -> bool:
        if not s : 
            return True

        pairs = {")": "(", "]": "[", "}": "{"}
        st = []
        for c in s :
            if c in pairs : 
                if not st or st[-1] != pairs[c]:
                    return False
                st.pop()
            else :  
                st.append(c)

        return not st