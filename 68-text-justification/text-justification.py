class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_line_length = 0

        for word in words:
            if current_line_length + len(word) + len(current_line) > maxWidth:
                # Time to justify the current line
                for i in range(maxWidth - current_line_length):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                result.append(''.join(current_line))
                current_line = []
                current_line_length = 0
            current_line.append(word)
            current_line_length += len(word)
        
        # Handle the last line
        result.append(' '.join(current_line).ljust(maxWidth))

        return result

        