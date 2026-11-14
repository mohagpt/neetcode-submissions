from collections import defaultdict
import heapq

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)


        patterns = defaultdict(list)
        minHeap = []
        for st in words :
            heapq.heappush(minHeap, (len(st), st)) 
            for i in range(len(st)) : 
                patterns[st[:i] + "*" + st[i+1:]].append(st)

        longestChain = 0
        visited = set()                          # was `set` (the class), needs ()
        chain = defaultdict(lambda: 1)
        
        while minHeap : 
            length, st = heapq.heappop(minHeap)
            if st in visited : 
                continue
            visited.add(st)

            crtLen = chain[st]
            longestChain = max(longestChain, crtLen)

            for i in range(length + 1) : 
                for neigh in patterns[st[:i] + "*" + st[i:]] : 
                    chain[neigh] = max(chain[neigh], crtLen + 1)


        return longestChain