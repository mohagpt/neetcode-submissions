class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set(wordList)
        if endWord not in words:
            return 0
        by_pattern = defaultdict(list)             # "h*t" -> ["hot", "hit", ...]
        for word in words | {beginWord}:
            for i in range(len(word)):
                by_pattern[word[:i] + "*" + word[i + 1:]].append(word)
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                for nxt in by_pattern[pattern]:
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, length + 1))
                by_pattern[pattern] = []           # a bucket only needs one visit
        return 0