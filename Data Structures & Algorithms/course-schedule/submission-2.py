class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        coursesTaken = 0 

        coursesTakenBefore = defaultdict(list)
        
        for c1,c2 in prerequisites : 
            coursesTakenBefore[c1].append(c2)
        
        visitedSet = set() 
        def dfs(crtCourse ) : 
            if crtCourse in visitedSet : 
                return False 
            if  coursesTakenBefore[crtCourse] == [] : 
                return True
            
            visitedSet.add(crtCourse)
            for pre in coursesTakenBefore[crtCourse]: 
                if not dfs(pre) : return False
            
            visitedSet.remove(crtCourse)
            coursesTakenBefore[crtCourse] = []
            return True

                
        for crs in range(numCourses) : 
            if not dfs(crs) : return False

        return True