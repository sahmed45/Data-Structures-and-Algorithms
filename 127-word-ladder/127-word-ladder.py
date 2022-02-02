class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        neighbors = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)
        

        visited = set([beginWord])
        q = deque([beginWord])
        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return count
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighboringWord in neighbors[pattern]:
                        if neighboringWord not in visited:
                            visited.add(neighboringWord)
                            q.append(neighboringWord)
            count += 1
            
        return 0
        
    
            