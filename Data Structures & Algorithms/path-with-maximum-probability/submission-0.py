class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        #first build adj list
        adjList = defaultdict(list)
        for i, edge in enumerate(edges) : 
            st, nd = edge
            adjList[st].append((succProb[i], nd))
            adjList[nd].append((succProb[i], st))

        #bfs starting from node start_node 
        max_heap = [(-1, start_node)]
        visited = set()
        while max_heap : 
            prob, crtNode = heapq.heappop(max_heap)
            prob = -prob
            if crtNode in visited : 
                continue
            visited.add(crtNode)
            if crtNode == end_node : 
                return prob
            for pb, neigh in adjList[crtNode] : 
                heapq.heappush(max_heap, (- prob * pb, neigh))
                        
        return 0