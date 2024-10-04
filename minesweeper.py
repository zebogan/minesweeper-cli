import numpy

GAME_SIZE = (14, 18)
NUM_MINES = 40

def init():
    mines = numpy.zeros(GAME_SIZE)
    for i in range(NUM_MINES):
        random_index1 = numpy.random.randint(0, mines.shape[0])
        random_index2 = numpy.random.randint(0, mines.shape[1])
        if mines[random_index1, random_index2] != 1:
            mines[random_index1, random_index2] = 1

    grid = numpy.zeros((mines.shape[0], mines.shape[1]), dtype=int)
    for iy, ix in numpy.ndindex(grid.shape):
        if mines[iy, ix] == 0:
            if iy == 0 and ix == 0:
                grid[0, 0] = mines[0][0:2].sum() + mines[1][0:2].sum()
            elif iy == GAME_SIZE[0] - 1 and ix == GAME_SIZE[1] - 1:
                grid[GAME_SIZE[0] - 1, GAME_SIZE[1] - 1] = mines[GAME_SIZE[0] - 2][(GAME_SIZE[1] - 2):GAME_SIZE[1]].sum() + mines[GAME_SIZE[0] - 1][(GAME_SIZE[1] - 2):GAME_SIZE[1]].sum()
            elif iy == 0 and ix == GAME_SIZE[1] - 1:
                grid[0, GAME_SIZE[1] - 1] = mines[0][(GAME_SIZE[1] - 2):GAME_SIZE[1]].sum() + mines[1][(GAME_SIZE[1] - 2):GAME_SIZE[1]].sum()
            elif iy == GAME_SIZE[0] - 1 and ix == 0:
                grid[GAME_SIZE[0] - 1, 0] = mines[GAME_SIZE[0] - 2][0:2].sum() + mines[GAME_SIZE[0] - 1][0:2].sum()
            
            elif iy == 0 and ix != 0 and ix != GAME_SIZE[1] - 1:
                grid[0, ix] = mines[0][(ix - 1):(ix + 2)].sum() + mines[1][(ix - 1):(ix + 2)].sum()
            elif iy == GAME_SIZE[0] - 1 and ix != 0 and ix != GAME_SIZE[1] - 1:
                grid[GAME_SIZE[0] - 1, ix] = mines[GAME_SIZE[0] - 2][(ix - 1):(ix + 2)].sum() + mines[GAME_SIZE[0] - 1][(ix - 1):(ix + 2)].sum()

            elif iy != 0 and iy != GAME_SIZE[0] - 1 and ix == 0:
                grid[iy, 0] = mines[iy - 1][0:2].sum() + mines[iy][0:2].sum() + mines[iy + 1][0:2].sum()
            elif iy != 0 and iy != GAME_SIZE[0] - 1 and ix == GAME_SIZE[1] - 1:
                grid[iy, GAME_SIZE[1] - 1] = mines[iy - 1][(GAME_SIZE[1] - 2):GAME_SIZE[1]].sum() + mines[iy][(GAME_SIZE[1] - 2):GAME_SIZE[1]].sum() + mines[iy + 1][(GAME_SIZE[1] - 2):GAME_SIZE[1]].sum()

            else:
                grid[iy, ix] = mines[iy - 1][(ix - 1):(ix + 2)].sum() + mines[iy][(ix - 1):(ix + 2)].sum() + mines[iy + 1][(ix - 1):(ix + 2)].sum()
        else:
            grid[iy, ix] = -1
    
    return mines, grid

def flood_fill(arr):
    rows, cols = arr.shape
    label = 1  # Starting label for tagging
    visited = numpy.zeros(arr.shape, dtype=bool)  # To keep track of visited cells

    def dfs(r, c, label):
        # Stack for the DFS
        stack = [(r, c)]
        
        while stack:
            x, y = stack.pop()
            if (x < 0 or x >= rows or
                y < 0 or y >= cols or
                visited[x, y] or
                arr[x, y] != 0):
                continue
            
            # Mark the cell as visited and tag it
            visited[x, y] = True
            arr[x, y] = label

            # Check all 4 possible directions (up, down, left, right)
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

    for r in range(rows):
        for c in range(cols):
            if arr[r, c] == 0 and not visited[r, c]:
                dfs(r, c, label)
                label += 1  # Increment the label for the next group

    return arr