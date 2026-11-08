class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, trgt, time in times:
            adj[src].append((trgt, time))

        dist = {}
        heap = [(0, k)]                       # (time to reach the node, node)
        while heap:
            t, node = heapq.heappop(heap)
            if node in dist:                  # already finalized with a smaller time
                continue
            dist[node] = t
            for nxt, w in adj[node]:
                if nxt not in dist:
                    heapq.heappush(heap, (t + w, nxt))

        return max(dist.values()) if len(dist) == n else -1