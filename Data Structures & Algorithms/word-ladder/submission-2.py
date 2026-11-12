class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words : 
            return 0 

        patterns = defaultdict(list)
        for w in words : 
            for i in range(len(w)) : 
                patterns[w[:i] + "*" + w[i + 1:]].append(w)

        queue = deque([beginWord])
        visited = {beginWord}
        length = 1

        while queue : 
            for _ in range(len(queue)) : 
                w = queue.popleft()
                if w == endWord : 
                    return length
                for i in range(len(w)) : 
                    for nxt in patterns[w[:i] + "*" + w[i + 1:]] : 
                        if nxt not in visited : 
                            visited.add(nxt)
                            queue.append(nxt)
            length += 1
        return 0 
        