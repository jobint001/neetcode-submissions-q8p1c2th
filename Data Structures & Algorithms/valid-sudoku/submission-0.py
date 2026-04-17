class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tempSet = set()

        for i in range(0,9):
            tempSet=set()
            for j in range(0,9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in tempSet:
                    print("1")
                    return False
                else:
                    tempSet.add(board[i][j])

        for i in range(0,9):
            tempSet=set()
            for j in range(0,9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in tempSet:
                    print("2")
                    return False
                else:
                    tempSet.add(board[j][i])
        j,k=0,0
        for i in range(0, 9):
            tempSet = set()
            for row in range(j,j+3):
                for col in range(k,k+3):
                    print("row "+str(row))
                    print("col "+str(col))
                    print(" ")
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in tempSet:
                        print("3")
                        return False
                    else:
                        tempSet.add(board[row][col])
            print("i " + str(i))
            if i in(0,1,3,4,6,7):
                k+=3
            else:
                k=0
                j+=3
        
        return True