class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])
        while queue:
            current_word, level = queue.popleft()
            
            if current_word == endWord:
                return level
            
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word in word_set:
                        queue.append((next_word, level + 1))
                        word_set.remove(next_word)
        
        return 0        
        