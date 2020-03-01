
N = 4
  
# A utility function to print solution matrix sol 
def print_solution( sol ): 
      
    for i in sol: 
        for j in i: 
            print(str(j) + " ", end ="") 
        print("") 

def is_safe(maze, x, y):
    if 0 <= x and x < N and 0 <= y and y < N and maze[x][y] == 1:
        return True
    return False

def solve_maze_util(maze, x, y, sol):
    # import pdb; pdb.set_trace()
    if is_safe(maze, x, y) == True:
        sol[x][y] = 1
        if x == N-1 and y == N-1:
            return True

    if is_safe(maze, x+1, y):
        return solve_maze_util(maze,x+1,y,sol)
    elif is_safe(maze, x, y+1):
        return solve_maze_util(maze,x,y+1,sol)

    return False

def solveMaze(maze):
    sol = [[0 for i in range(N)] for i in range(N)]

    if solve_maze_util(maze,0,0,sol):
        print_solution(sol)
    else:
        print("No soution")
        print_solution(sol)

if __name__ == "__main__": 
    # Initialising the maze 
    maze = [ [1, 0, 0, 0], 
             [1, 1, 1, 1], 
             [0, 0, 0, 1], 
             [1, 1, 1, 0] ] 
               
    solveMaze(maze) 