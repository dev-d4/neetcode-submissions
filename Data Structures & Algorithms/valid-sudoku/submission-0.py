class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        board_box = [[] for x in range(9)]
        for i in range(9):
            if i<3:
                i_count = 0
            elif i<6:
                i_count = 3
            elif i<9:
                i_count = 6
            
            for j in range(9):
                if j<3:
                    j_count = 0
                elif j<6:
                    j_count = 1
                elif j<9:
                    j_count = 2
            
                i_box = i_count+j_count
                board_box[i_box].append(board[i][j])


        board_col = [[] for x in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                board_col[j].append(val)

        validated = True
        for i in range(9):
            normal_check = []
            col_check = []
            box_check = []
            for j in range(9):
                val_normal = board[i][j]
                if val_normal.isnumeric() and val_normal in normal_check:
                    validated = False
                    return validated
                normal_check.append(val_normal)

                val_col = board_col[i][j]
                if val_col.isnumeric() and val_col in col_check:
                    validated = False
                    return validated
                col_check.append(val_col)

                val_box = board_box[i][j]
                if val_box.isnumeric() and val_box in box_check:
                    validated = False
                    return validated
                box_check.append(val_box)

        return validated