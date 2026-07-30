# https://leetcode.com/problems/valid-sudoku/description/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # loop rows
        rows = [0] * 9

        for r in board:
            for num in r:
                if num == "1":
                    if rows[0] == 1:
                        return False
                    rows[0] += 1

                if num == "2":
                    if rows[1] == 1:
                        return False
                    rows[1] += 1

                if num == "3":
                    if rows[2] == 1:
                        return False
                    rows[2] += 1

                if num == "4":
                    if rows[3] == 1:
                        return False
                    rows[3] += 1

                if num == "5":
                    if rows[4] == 1:
                        return False
                    rows[4] += 1

                if num == "6":
                    if rows[5] == 1:
                        return False
                    rows[5] += 1

                if num == "7":
                    if rows[6] == 1:
                        return False
                    rows[6] += 1

                if num == "8":
                    if rows[7] == 1:
                        return False
                    rows[7] += 1

                if num == "9":
                    if rows[8] == 1:
                        return False
                    rows[8] += 1

            rows = [0] * 9

        # loop cols
        cols = [0] * 9

        for c in range(9):
            for r in range(9):
                if board[r][c] == "1":
                    if cols[0] == 1:
                        return False
                    cols[0] += 1

                if board[r][c] == "2":
                    if cols[1] == 1:
                        return False
                    cols[1] += 1

                if board[r][c] == "3":
                    if cols[2] == 1:
                        return False
                    cols[2] += 1

                if board[r][c] == "4":
                    if cols[3] == 1:
                        return False
                    cols[3] += 1

                if board[r][c] == "5":
                    if cols[4] == 1:
                        return False
                    cols[4] += 1

                if board[r][c] == "6":
                    if cols[5] == 1:
                        return False
                    cols[5] += 1

                if board[r][c] == "7":
                    if cols[6] == 1:
                        return False
                    cols[6] += 1

                if board[r][c] == "8":
                    if cols[7] == 1:
                        return False
                    cols[7] += 1

                if board[r][c] == "9":
                    if cols[8] == 1:
                        return False
                    cols[8] += 1

            cols = [0] * 9

        # loop 3x3 boxes
        boxes = [0] * 9

        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        if board[r][c] == "1":
                            if boxes[0] == 1:
                                return False
                            boxes[0] += 1

                        if board[r][c] == "2":
                            if boxes[1] == 1:
                                return False
                            boxes[1] += 1

                        if board[r][c] == "3":
                            if boxes[2] == 1:
                                return False
                            boxes[2] += 1

                        if board[r][c] == "4":
                            if boxes[3] == 1:
                                return False
                            boxes[3] += 1

                        if board[r][c] == "5":
                            if boxes[4] == 1:
                                return False
                            boxes[4] += 1

                        if board[r][c] == "6":
                            if boxes[5] == 1:
                                return False
                            boxes[5] += 1

                        if board[r][c] == "7":
                            if boxes[6] == 1:
                                return False
                            boxes[6] += 1

                        if board[r][c] == "8":
                            if boxes[7] == 1:
                                return False
                            boxes[7] += 1

                        if board[r][c] == "9":
                            if boxes[8] == 1:
                                return False
                            boxes[8] += 1

                boxes = [0] * 9

        return True
