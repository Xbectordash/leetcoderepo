class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = {}

        # Count the frequency of each word in the list of words
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        def is_valid(start):
            seen = {}
            for i in range(num_words):
                word_start = start + i * word_len
                word = s[word_start:word_start + word_len]
                if word not in word_count:
                    return False
                if word in seen:
                    seen[word] += 1
                else:
                    seen[word] = 1
                if seen[word] > word_count[word]:
                    return False
            return True

        result = []
        for i in range(min(word_len, len(s) - total_len + 1)):
            for j in range(i, len(s) - total_len + 1, word_len):
                if is_valid(j):
                    result.append(j)
        
        return result
        