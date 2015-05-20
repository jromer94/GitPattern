import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(1)
screen.addstr("Select highlighted blocks with i\n")
screen.addstr("xxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
for x in range(0,7):
    screen.addstr("x                         x\n")
screen.addstr("xxxxxxxxxxxxxxxxxxxxxxxxxxx\n")

while True:
    event = screen.getch()
    yx = screen.getyx()
    if event == curses.KEY_RIGHT:
        if yx[1] < 25:
            screen.move(yx[0], yx[1] + 1)
    elif event == curses.KEY_LEFT:
        if yx[1] > 1:
            screen.move(yx[0], yx[1] - 1)
    elif event == curses.KEY_DOWN:
        if yx[0] < 8: 
            screen.move(yx[0] + 1, yx[1])
    elif event == curses.KEY_UP:
        if yx[0] > 2:
            screen.move(yx[0] - 1, yx[1])
    elif event == ord("i"):
        screen.chgat(1, curses.A_STANDOUT)
