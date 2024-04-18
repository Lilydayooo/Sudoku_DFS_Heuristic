from DFS_Sudoku import DFS_solve
from Heuristics_Sudoku import H_Solve

print ("\n\nTesting on 9x9 grid") # around 23 minutes for a DFS with heuristic
grid = [[0,1,0,0,0,0,3,7,0],
        [3,0,0,0,0,7,0,4,0],
        [0,0,0,8,0,4,0,0,2],
        [0,0,4,0,0,0,6,3,0],
        [0,0,0,0,0,0,0,0,1],
        [0,8,3,0,0,0,0,0,5],
        [8,0,0,9,0,0,0,6,4],
        [9,4,0,2,0,0,8,0,3],
        [0,0,2,0,8,5,9,1,0]]

DFS_solve(grid)
# H_Solve(grid) 