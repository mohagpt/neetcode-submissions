class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        answer = 0
        for start in range(len(bombs)):
            seen = {start}
            queue = [start]
            for i in queue:
                x,y,r = bombs[i]
                for j,(xx,yy,_) in enumerate(bombs):
                    if j not in seen and (x-xx)**2 + (y-yy)**2 <= r*r:
                        seen.add(j)
                        queue.append(j)
            answer = max(answer,len(seen))
        return answer
