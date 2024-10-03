import curses, numpy

GAME_SIZE = (14, 18)

mines = numpy.zeros(GAME_SIZE)
for i in range(40):
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

stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.nodelay(True)
stdscr.keypad(True)

stdscr.refresh()

key = ''
while True:
    key = stdscr.getch()

    if key != -1:
        stdscr.clear()
        stdscr.addstr(str(mines) + "\n\n" + str(grid))
        if key == curses.KEY_UP or key == 119:
            stdscr.addstr("up")
        elif key == curses.KEY_DOWN or key == 115:
            stdscr.addstr("down")
        elif key == curses.KEY_LEFT or key == 97:
            stdscr.addstr("left")
        elif key == curses.KEY_RIGHT or key == 100:
            stdscr.addstr("right")
        elif key == 32:
            stdscr.addstr("sweep")
        elif key == 102:
            stdscr.addstr("flag")
        else:
            stdscr.addstr(str(key))

    stdscr.refresh()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
stdscr.nodelay(False)
curses.endwin()