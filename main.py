import curses, numpy, minesweeper

minesweeper.GAME_SIZE = (14, 18)
minesweeper.NUM_MINES = 40

mines, grid = minesweeper.init()
flag = numpy.zeros((grid.shape[0], grid.shape[1]))

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
while True:
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
        elif key == 32:
            stdscr.addstr("sweep")
        elif key == 102:
            stdscr.addstr("flag")
        else:
            stdscr.addstr(str(key))

    for y, x in numpy.ndindex(grid.shape):
        if grid[y, x] == 0:
            stdscr.addstr(y, x*2, "*")
    stdscr.move(cursorPos[1], cursorPos[0] * 2)

    stdscr.refresh()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
stdscr.nodelay(False)
curses.endwin()