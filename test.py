import sys
import os
start = 0
x = 5
y = 4
size = [12, 7]
line = ["+----------+",
        "|          |",
        "|          |",
        "|          |",
        "|          |",
        "|          |",
        "+----------+"]
def printline():
    # os.system('clear')
    sys.stderr.write("\x1b[2J\x1b[H")
    for current in line:
        print current
#    sys.stdout.flush()

def lineman(xx, yy, new):
    curr = list(line[yy])
    curr[xx] = new
    curr = "".join(curr)
    line[yy] = curr
    printline()


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#print getch()

def control():
    global x
    global y
    lineman(x,y, "@")
    inp = raw_input()
#    inp = getch()
    print inp
    if inp not in ["w", "a", "s", "d"]:
        print "Invalid input"
    elif inp == "q":
        sys.exit()
        return 1
    elif inp == "w":
        y+=1
        if y > 6:
            y = 0
        lineman(x,y, "@")
    elif inp == "a":
        x-=1
        if x < 0:
            x = 11
        lineman(x,y, "@")

while True:
    if control() == 1:
        sys.exit()
        break
sys.exit()
