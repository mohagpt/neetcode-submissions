from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for start in range(len(graph)):        # the graph may be disconnected
            if start in color:
                continue
            color[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for nxt in graph[node]:
                    if nxt not in color:
                        color[nxt] = 1 - color[node]
                        queue.append(nxt)
                    elif color[nxt] == color[node]:    # both ends of an edge on the same side
                        return False
        return True
