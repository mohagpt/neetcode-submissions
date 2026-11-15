class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = [0] * len(heights) 
        crtSt = []

        for i in range(len(heights) -1, -1 , -1) : 
            canSee = 0 
            while crtSt and crtSt[-1] < heights[i] : 
                canSee += 1
                crtSt.pop()
            if crtSt : 
                canSee += 1
            crtSt.append(heights[i])
            answer[i] = canSee
        
        return answer