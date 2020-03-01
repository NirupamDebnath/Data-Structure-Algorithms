n =8

def isPossible(board,x,y):
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
        return True
    else:
        return False

def solveKTUtil(board,x,y,movex,movey,pos):
    if pos > 62:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" | ")
            print()
            print("-"* 5*n)
    if pos == n**2:
        return True
    
    for i in range(8): 
        new_x = x + movex[i] 
        new_y = y + movey[i]
        # import pdb; pdb.set_trace()
        if(isPossible(board, new_x, new_y)): 
            board[new_x][new_y] = pos 
            if(solveKTUtil(board,new_x,new_y,movex,movey,pos+1)): 
                return True
              
            # Backtracking 
            board[new_x][new_y] = -1
    return False
    


def solveKT():
    board =[[-1 for i in range(n)] for i in range(n)]

    movex = [2, 2,-2,-2, 1, 1,-1,-1]
    movey = [1,-1, 1,-1,-2, 2, -2,2]

    pos = 1

    board[0][0] = 0

    solveKTUtil(board, 0, 0, movex, movey, pos)

    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" | ")
        print()
        print("-"* 5*n)

if __name__ == "__main__":
    solveKT()