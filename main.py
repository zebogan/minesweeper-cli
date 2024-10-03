import curses, numpy, minesweeper

minesweeper.GAME_SIZE = (14, 18)
minesweeper.NUM_MINES = 40

mines, grid = minesweeper.init()

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