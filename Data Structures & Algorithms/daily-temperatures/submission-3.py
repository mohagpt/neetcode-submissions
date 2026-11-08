class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) -1, -1, -1) :
            if not stack : 
                stack.append([temperatures[i], i]) 
                continue
            while stack and stack[-1][0] <= temperatures[i]: 
                stack.pop()
            if not stack : 
                res[i] = 0
            else :
                res[i] = stack[-1][1] - i 
            stack.append([temperatures[i], i])   
        return res