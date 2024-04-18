from DFS_Sudoku import DFS_solve
from Heuristics_Sudoku import H_Solve

print ("\n\nTesting on 9x9 grid")
grid = [[0,6,7,0,9,0,0,8,0],
        [3,0,0,0,0,0,0,0,0],
        [0,0,0,7,8,1,0,0,0],
        [0,0,8,0,0,0,0,0,9],
        [0,0,0,0,0,0,0,4,3],
        [5,7,0,6,0,0,0,0,0],
        [0,0,0,0,0,0,8,3,4],
        [0,0,4,0,0,9,0,5,2],
        [0,0,0,0,1,0,0,6,0]]

DFS_solve(grid)
# H_Solve(grid) 