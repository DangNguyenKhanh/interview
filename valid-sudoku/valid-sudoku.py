class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1. Validate all Rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # 2. Validate all Columns
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # 3. Validate all nine 3x3 Sub-boxes
        # (br, bc) represent the top-left corner of each sub-box
        for br in (0, 3, 6):
            for bc in (0, 3, 6):
                seen = set()
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        val = board[r][c]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return True
