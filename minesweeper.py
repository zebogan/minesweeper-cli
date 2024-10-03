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

    grid = numpy.zeros((mines.shape[0], mines.shape[1]))
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
    
    return mines, grid
