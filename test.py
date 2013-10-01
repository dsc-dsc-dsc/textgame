import sys
import os
start = 0
x = 5
y = 4
size = [73, 57]
def genbox(size = size):
    size[0]=size[0]-2
    size[1]=size[1]-2
    line0 = ''.join(["+", "-"*size[0], "+"])
    line1 = ''.join(["|", " "*size[0], "|"])
    finbox = [line1]*size[1]
    finbox.append(line0)
    finbox.insert(0, line0)
    
#    print finbox
    return finbox
line = genbox()
def printline():
    #os.system('clear')
    print chr(27) + "[2J"
    #sys.stderr.write("\x1b[2J\x1b[H")
    for current in line:
        print current
    sys.stdout.flush()

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

def control(inp):
    global x
    global y
    global size
    lineman(x,y, " ")
#    inp = raw_input()
#    inp = getch()
    print inp
    if inp not in ["w", "a", "s", "d", "zz", "q"]:
        print "Invalid input"
    elif inp == "q":
        sys.exit(1)
        line = ['x','x']
        return 1
    elif inp == "w":
        y-=1
        if y < 0:
            y = size[1] + 1
        lineman(x,y, "w")
    elif inp == "d":
        x+=1
        if x > size[0] + 1:
            x = 0
        lineman(x,y, "d")
    elif inp == "s":
        y+=1
        if y > size[1] + 1:
            y = 0
        lineman(x,y, "s")
    elif inp == "a":
        x-=1
        if x < 0:
            x = size[0] + 1
        lineman(x,y, "a")
inp = "zz"
control(inp)
while inp != "q":
    inp = getch()
    control(inp)
sys.exit()
