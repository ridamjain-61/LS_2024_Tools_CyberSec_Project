# flag=flag{f34r1355_5ud0ku_c0nqu3r0r}

from pwn import *
import numpy as np

io=process('./sudoku')
context.log_level='critical'
# starting the process and ignoring unnecessary messages
for l in range(420):
    print(io.recvline(1).decode("utf-8"))
    print(io.recvline(1).decode("utf-8"))
    print(io.recvline(1).decode("utf-8"))

    # some starting messages.

    puz=np.zeros((9,9))
    # this numpy array will store our sudoku
    # print(puz)
    # building on puz
    k=0
    while k<=8:
        
        list=io.recvline(1).decode("utf-8")
        # print(list)
        if list[1]=='-':
            continue
        i=0
        j=0
        while i<=8:
            if list[j]=='.':
                puz[k][i]=0
                i+=1
                j+=1
            elif (list[j]==" " or list[j]=="|" ):
                j+=1
            else:
                puz[k][i]=list[j]
                i+=1
                j+=1
        k+=1


    # print(puz)
    puz2=puz.copy()
    # making a copy of puz. Used later.
    # sudoku extraction done.

    def is_valid(board, row, col, num):
        # checks if the number is not in the current row, column, and 3x3 subgrid
        # basically if the code is valid.
        if num in board[row, :] or num in board[:, col]:
            return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        if num in board[start_row:start_row+3, start_col:start_col+3]:
            return False

        return True

    def solve_sudoku(board):
        for row in range(9):
            for col in range(9):
                if board[row, col] == 0:  # Find an empty spot
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row, col] = num

                            if solve_sudoku(board):
                                return True
                                # recursive algo.

                            board[row, col] = 0  # reset if false and check again

                    return False  #backtracking
        return True

    solve_sudoku(puz)
        # print(puz)
        # puz is updated as fully solved

    puz2=puz-puz2
    # now puz2 contains only the moves we need to make. rest are zero.
    moves_rq=[]
    for row in range(9):
        for col in range(9):
            if puz2[row][col]>0:
                moves_rq.append([row,col,int(puz2[row][col])])

    print(io.recvline(1).decode("utf-8"))
    # print(len(moves_rq))
    for i in range(len(moves_rq)):
        
        curr=str(moves_rq[i][0])+" "+str(moves_rq[i][1])+" "+str(moves_rq[i][2])
        # print(curr)
        io.sendline(curr)
        # sending the moves required to the process.
        for j in range(14):
            io.recvline(1).decode("utf-8")
    
        
    print(io.recvline(1).decode("utf-8"))    
    print(io.recvline(1).decode("utf-8"))




print(io.recvline(1).decode("utf-8"))
print("All Sudoku puzzles solved!!!")

