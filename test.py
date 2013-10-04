import sys
import os
import random
import termsiz
import time
start = 0
moves = 1000000000000000000
size = [termsiz.get_terminal_width(), termsiz.get_terminal_height() - 2]
x = size[0]//2
y = size[1]//2
def getsize():
    size = [termsiz.get_terminal_width(), termsiz.get_terminal_height() - 2]
    return size
score = 0
def genbox(size = size):
    size[0]=size[0]-2
    size[1]=size[1]-2
    line0 = ''.join(["+", "-"*size[0], "+"])
    line1 = ''.join(["|", " "*size[0], "|"])
    finbox = [line1]*size[1]
    finbox.append(line0)
    finbox.insert(0, line0)
    return finbox
line = genbox()
def printline(msg = ""):
    for current in line:
        print(current)
    print(msg)
    #sys.stdout.flush()
error = ""
def lineman(xx, yy, new, collide = False):
    global score
    global error
    curr = list(line[yy])
    print(curr)
    if curr[xx] == "@":
        error = "You can't do that!"
        return 1
    if curr[xx] == ".":
        score+=1
    curr[xx] = new
    curr = "".join(curr)
    line[yy] = curr
    if new == "@":
        printline("Generating objects")
        return
    if collide == False:
        error = ""
    printline("Score: "+ str(score) +"  Moves Remaining: " + str(moves) + "  " + error)

def lineinf():
    #print list(line[y])
    #time.sleep(1)
    if "." in list(line[y]):
        return line[y].index(".")
    else:
        return False

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

def control(inp):
    global x
    global y
    global size
    lineman(x,y, " ")
    if inp not in ["w", "a", "s", "d", "  ", "q", ""]:
        printline("Invalid input")
    elif inp == "q" or inp == "":
        sys.exit(1)
        line = ['x','x']
        return 1
    elif inp == "w":
        y-=1
        if y < 1:
            y = size[1] - 2
        if lineman(x,y, "w") == 1:
            y+=1
            lineman(x,y, "w", True)
            return 1
        else:
            return 0
    elif inp == "d":
        x+=1
        if x > size[0] - 2:
            x = 1
        if lineman(x,y, "d") == 1:
            x-=1
            lineman(x,y, "d", True)
            return 2
        else:
            return 0
    elif inp == "s":
        y+=1
        if y > size[1] - 2:
            y = 1
        if lineman(x,y, "s") == 1:
            y-=1
            lineman(x,y, "s", True)
            return 3
        else:
            return 0
    elif inp == "a":
        x-=1
        if x < 1:
            x = size[0] - 2
        if lineman(x,y, "a") == 1:
            x+=1
            lineman(x,y, "a", True)
            return 4
        else:
            return 0
inp = "  "
def AI(c=False):
    global x, moves
    a = control(random.choice(["a","s","d","w"]))
    if a == 1:
        time.sleep(0.1)
        control("s")
    elif a == 2:
        time.sleep(0.1)
        control("a")
    elif a == 3:
        time.sleep(0.1)
        control("w")
    elif a == 4:
        time.sleep(0.1)
        control("d")
    else:
        #for i in range(0,random.randint(1,30)):
        #if c == 0:
        info = lineinf()
        #print info
        #time.sleep(1)
        #moves -=1
        if info != False or c == True:
            if info > x:
                for z in range(0,info-x):
                    time.sleep(0.1)
                    control("d")
                    moves-=1
            #    c == True
            elif info < x:
                for z in range(0,x-info):
                    time.sleep(0.1)
                    control("a")
                    moves-=1
            #    c == True
        else:
            control(random.choice(["a","s","d","w"]))
            moves -=1
        time.sleep(0.1)

def genthings(char, upper):
    for i in range(random.randint(upper//2, upper)):
        lineman(random.randint(1,size[0]),random.randint(1,size[1]), char)
genthings("@", 100)
genthings(".", 100)
score = 0
control(inp)
#AI()
while inp != "q" and moves > 0:
    AI()
    #inp = getch()
    time.sleep(0.1)
    #control(inp)
    size = getsize()
    #print int(time.time())
    moves-=1
while inp != "q" or moves < 0:
    line = genbox()

sys.exit()
