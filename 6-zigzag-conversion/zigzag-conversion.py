class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # Initialize an array of strings to hold rows
        rows = [''] * numRows
        current_row = 0
        direction = 1  # Direction: 1 for down, -1 for up

        for char in s:
            rows[current_row] += char
            if current_row == 0:
                direction = 1  # Change direction to down if at top row
            elif current_row == numRows - 1:
                direction = -1  # Change direction to up if at bottom row
            current_row += direction

        # Join all rows to form the final zigzag pattern string
        zigzag_string = ''.join(rows)
        return zigzag_string
        