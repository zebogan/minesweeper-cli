import curses, numpy, minesweeper

minesweeper.GAME_SIZE = (14, 18)
minesweeper.NUM_MINES = 40

mines, grid = minesweeper.init()
flag = numpy.zeros((grid.shape[0], grid.shape[1]))
revealed = numpy.zeros((grid.shape[0], grid.shape[1]))

zeroGroups = numpy.copy(grid)
minesweeper.flood_fill(zeroGroups)

for iy, ix in numpy.ndindex(zeroGroups.shape):
    if grid[iy, ix] != 0:
        zeroGroups[iy, ix] = 0

loss = False
going = True

stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
stdscr.nodelay(True)
stdscr.keypad(True)

stdscr.refresh()

cursorPos = [0, 0]

key = ''
while going:
    key = stdscr.getch()

    if key != -1:
        stdscr.clear()
        if key == curses.KEY_UP or key == 119:
            cursorPos[1] -= 1
        elif key == curses.KEY_DOWN or key == 115:
            cursorPos[1] += 1
        elif key == curses.KEY_LEFT or key == 97:
            cursorPos[0] -= 1
        elif key == curses.KEY_RIGHT or key == 100:
            cursorPos[0] += 1
        elif key == 32: # sweep (space)
            revealed[cursorPos[1], cursorPos[0]] = 1
            if grid[cursorPos[1], cursorPos[0]] == 0:
                currentZeroGroup = zeroGroups[cursorPos[1], cursorPos[0]]
                for iy, ix in numpy.ndindex(grid.shape):
                    if zeroGroups[iy, ix] == currentZeroGroup:
                        revealed[iy, ix] = 1
                        revealed = minesweeper.reveal_around(revealed, ix, iy)
        elif key == 102: # flag (f)
            if revealed[cursorPos[1], cursorPos[0]] == 0:
                flag[cursorPos[1], cursorPos[0]] = not flag[cursorPos[1], cursorPos[0]]
        if loss:
            going = False

    if not loss:
        for y, x in numpy.ndindex(revealed.shape):
            if revealed[y, x] == 0:
                stdscr.addstr(y, x*2, "#")
            else:
                if mines[y, x] == 1:
                    loss = True
                else:
                    stdscr.addstr(y, x*2, str(grid[y, x]))
            if flag[y, x] == 1:
                stdscr.addstr(y, x*2, "󰈻")
        stdscr.move(cursorPos[1], cursorPos[0] * 2)
    else:
        for y, x in numpy.ndindex(mines.shape):
            if mines[y, x] == 1:
                stdscr.addstr(y, x*2, "*")

    stdscr.refresh()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
stdscr.nodelay(False)
curses.endwin()

print(str(grid))
print(str(zeroGroups))