class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            digits = [c for c in row if c != '.']
            if len(digits) != len(set(digits)):
                return False

        for col in zip(*board):
            digits = [c for c in col if c != '.']
            if len(digits) != len(set(digits)):
                return False

        for i in (0, 3, 6):
            for j in (0, 3, 6):
                box = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                digits = [c for c in box if c != '.']
                if len(digits) != len(set(digits)):
                    return False

        return True


