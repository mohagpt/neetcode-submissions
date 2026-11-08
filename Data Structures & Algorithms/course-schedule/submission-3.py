from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        unlocks = defaultdict(list)          # pre -> courses it unlocks
        for crs, pre in prerequisites:
            unlocks[pre].append(crs)
            indegree[crs] += 1

        queue = deque(c for c in range(numCourses) if indegree[c] == 0)
        taken = 0
        while queue:
            c = queue.popleft()
            taken += 1
            for nxt in unlocks[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return taken == numCourses