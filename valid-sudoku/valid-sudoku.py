class Solution:  
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for line in board:
            hashmap = {}
            for n in line:
                if n.isdigit():
                    hashmap[n] = hashmap.get(n, 0) + 1
                    if hashmap[n] > 1:
                        return False
        for i in range(9):
            hashmap = {}
            for j in range(9):
                if board[j][i].isdigit():
                    hashmap[board[j][i]] = hashmap.get(board[j][i], 0) + 1
                    if hashmap[board[j][i]] > 1:
                        return False
        for i in range(9):
            hashmap = {}
            for a in range(3):
                for b in range(3):
                    n = board[(i * 3 + a) % 9][i//3 * 3 + b]
                    if n.isdigit():
                        hashmap[n] = hashmap.get(n, 0) + 1
                        if hashmap[n] > 1:
                            return False
        return True