class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hist = {str(x): 0 for x in range (1,10)}
        hist_cpy1 = hist.copy()
        hist_cpy2 = hist.copy()
        hist_cpy3 = {(str(x),str(y)): hist.copy() for x in range(3) for y in range(3)}

        for i in range (9):
            
            for j in range (9):
                if board[i][j].isdigit():
                    hist_cpy1[board[i][j]] += 1
                    hist_cpy3[(str(i // 3), str(j // 3))][board[i][j]] += 1
                    if hist_cpy3[(str(i // 3), str(j // 3))][board[i][j]] > 1:
                        return False
                if board[j][i].isdigit(): hist_cpy2[board[j][i]] += 1
            
            if max(hist_cpy1.values()) > 1 or max(hist_cpy2.values()) > 1:
                return False

            hist_cpy1 = hist.copy()
            hist_cpy2 = hist.copy()
        
        return True


               






        