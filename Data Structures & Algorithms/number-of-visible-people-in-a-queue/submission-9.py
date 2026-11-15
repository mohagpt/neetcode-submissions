class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = [0] * len(heights) 
        crtSt = []

        for i in range(len(heights) -1, -1 , -1) : 
            while crtSt and crtSt[-1] < heights[i] : 
                answer[i] += 1
                crtSt.pop()
            if crtSt : 
                answer[i] += 1
            crtSt.append(heights[i])
 
        
        return answer