class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preCourses = defaultdict(list)

        for a,b in prerequisites : 
            preCourses[a].append(b)
        
        done, visiting = set(), set()
        order = []
        def dfs(crs) :
            if crs in visiting :
                return False
            if crs in done :
                return True
            visiting.add(crs)
            for preCrs in preCourses[crs]:
                if not dfs(preCrs): return False
            visiting.remove(crs)
            done.add(crs)
            order.append(crs)         # all prerequisites are already in order
            return True
        
        for crs in range(numCourses) :
            if not dfs(crs) : return []
        return order
                 