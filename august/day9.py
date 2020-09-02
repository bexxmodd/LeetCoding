def orangesRotting(grid) -> int:
    x, y = 0, 0
    matrix_size = len(grid) * len(grid[0])
    oranges = []
    minutes = 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                x, y = i, j
            if grid[i][j] == 1:
                oranges.append([i, j])

    while (count < matrix_size):
        x_copy, y_copy = x, y
        if x == 0:
        if grid[x + 1][y] == 1:
            grid[x + 1][y] = 2
            x += 1
            minutes += 1
        if grid[x - 1]
    print(minutes)


orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
orangesRotting([0,2])