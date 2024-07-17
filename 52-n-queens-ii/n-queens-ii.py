class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if col in cols or (row - col) in major_diagonals or (row + col) in minor_diagonals:
                    continue
                cols.add(col)
                major_diagonals.add(row - col)
                minor_diagonals.add(row + col)
                backtrack(row + 1)
                cols.remove(col)
                major_diagonals.remove(row - col)
                minor_diagonals.remove(row + col)

        cols = set()
        major_diagonals = set()
        minor_diagonals = set()
        self.count = 0
        backtrack(0)
        return self.count

 
        