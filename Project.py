from tkinter import *
from turtle import *
import winsound

#Game over sound play function
def game_over():
    winsound.PlaySound("F:\hassan\gameover.wav", winsound.SND_ASYNC)

#Halt screen after every point
def halt():
    pass

#closes game
def Close():
    winsound.PlaySound("F:\hassan\selection.wav", winsound.SND_ASYNC)
    win.destroy()

# Instructions
def instructions():
    winsound.PlaySound("F:\hassan\selection.wav", winsound.SND_ASYNC)
    ins = Toplevel(win)
    ins.geometry("800x400")
    ins.configure(background="black")
    heading = Label(ins, text="INSTRUCTIONS", fg="red", bg="black", font=("calibri", 30, "bold"), justify=CENTER).pack(side=TOP)
    data = Label(ins, text="For Player 1:\n Use 'w' and 's' keys to move the paddle up and down respectively.\n\nFor Player 2:\n Use the 'Up' and 'Down' arrow keys to move the paddle up and down.\n\nDONOT press the keys when the ball is going to the other player!!",
                 fg="white", bg="black", font=("calibri", 20), justify=LEFT).pack()

# About
def About():
    winsound.PlaySound("F:\hassan\selection.wav", winsound.SND_ASYNC)
    abt = Toplevel(win)
    abt.geometry("1200x400")
    abt.configure(background="black")
    Data1 = Label(abt, text="ABOUT\n", fg="turquoise", bg="black", font=("calibri", 40, "bold"), justify=CENTER).pack(side=TOP)
    Data2 = Label(abt, text="Techlord was co-founded by Muhammad Hassan and Moiz Tariq in January 2020.\n\nInitially this gaming company has only two assistants, Syed Maaz and Muhammad Hassan Ahmed.\n\nTechlord has released its first ever product 'BOUNCE' on January 21, 2020.\n\nTechlord hopes to give its users the best gaming material in the near future.",
                  fg="white", bg="black", font=("calibri", 20), justify=LEFT).pack()


#Double Player
def double():
    winsound.PlaySound("F:\hassan\selection.wav", winsound.SND_ASYNC)
    global windows
    name_1 = inputname1.get().strip()            # Gets name of players entered in tkinter window
    name_2 = inputname2.get().strip()            # Gets name of players entered in tkinter window
    pl.withdraw()
    windows = Screen()                            # turtle screen
    windows.title("Bounce Game by TechLord")
    windows.bgcolor("white")
    windows.setup(width=1200, height=760)
    windows.tracer(0)

    # Score
    score_1 = 0
    score_2 = 0

    # paddle a
    pad_a = Turtle()
    pad_a.speed(0)
    pad_a.shape("square")
    pad_a.color("blue")
    pad_a.shapesize(stretch_wid=5, stretch_len=1)
    pad_a.penup()
    pad_a.goto(-550, 0)

    # paddle b
    pad_b = Turtle()
    pad_b.speed(0)
    pad_b.shape("square")
    pad_b.color("blue")
    pad_b.shapesize(stretch_wid=5, stretch_len=1)
    pad_b.penup()
    pad_b.goto(550, 0)

    # ball
    ball = Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("red")
    ball.shapesize(stretch_wid=1.2, stretch_len=1.2)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = -1

    # Pen for Score
    pen = Turtle()
    pen.speed(0)
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 330)
    pen.write("{}: 0  {}: 0".format(name_1, name_2), align="center", font=("Bebas Neue", 24, "italic"))             # Score board with player names and score

    # Function
    def pad_a_up():
        y = pad_a.ycor()
        if y <= 300:
            y += 40
        else:
            y = y
        pad_a.sety(y)

    def pad_a_down():
        y = pad_a.ycor()
        if y >= -300:
            y -= 40
        else:
            y = y
        pad_a.sety(y)

    def pad_b_up():
        y = pad_b.ycor()
        if y <= 300:
            y += 40
        pad_b.sety(y)

    def pad_b_down():
        y = pad_b.ycor()
        if y >= -300:
            y -= 40
        pad_b.sety(y)

    # keyboard binding
    windows.listen()
    windows.onkeypress(pad_a_up, "w")
    windows.onkeypress(pad_a_down, "s")
    windows.onkeypress(pad_b_up, "Up")
    windows.onkeypress(pad_b_down, "Down")

    # Main loop
    while score_1 < 5 and score_2 < 5:            # While none of the player score 10 points
        windows.update()                             # Updates the position of ball and paddles
        # moving ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # border checking

        # Top and Bottom
        if ball.ycor() > 370:
            ball.sety(370)
            ball.dy *= -1
            winsound.PlaySound("F:\hassan\wallhit.wav", winsound.SND_ASYNC)

        if ball.ycor() < -370:
            ball.sety(-370)
            ball.dy *= -1
            winsound.PlaySound("F:\hassan\wallhit.wav", winsound.SND_ASYNC)

        if ball.xcor() > 610:        # If ball missed by player on the right(i.e player b)
            windows.delay(5000)
            ball.goto(0, 0)
            ball.dx *= -1
            score_1 += 1
            pen.clear()
            pen.write("{}: {}  {}: {}".format(name_1, score_1, name_2, score_2), align="center", font=("Bebas Neue", 24, "italic"))
            winsound.PlaySound("F:\hassan\point.wav", winsound.SND_ASYNC)
            windows.ontimer(halt(), 2000)

        if ball.xcor() < -610:           # If ball missed by player on the left(i.e player a)
            windows.delay(5000)
            ball.goto(0, 0)
            ball.dx *= -1
            score_2 += 1
            pen.clear()
            pen.write("{}: {}  {}: {}".format(name_1, score_1, name_2, score_2), align="center",
                      font=("Bebas Neue", 24, "italic"))
            winsound.PlaySound("F:\hassan\point.wav", winsound.SND_ASYNC)
            windows.ontimer(halt(), 2000)


        # paddle and ball collisions
        if 540 < ball.xcor() < 550 and (
                pad_b.ycor() + 55 > ball.ycor() > pad_b.ycor() - 55):
            ball.setx(540)
            ball.dx *= -1
            winsound.PlaySound("F:\hassan\paddle.wav", winsound.SND_ASYNC)          # Added sound
        if -540 > ball.xcor() > -550 and (
                pad_a.ycor() + 55 > ball.ycor() > pad_a.ycor() - 55):
            ball.setx(-540)
            ball.dx *= -1
            winsound.PlaySound("F:\hassan\paddle.wav", winsound.SND_ASYNC)
    if score_1 == 5:
        windows.ontimer(game_over(), 2000)          # Halts the screen for 2 seconds/2000 milliseconds and runs a function
        res = Toplevel(win)           # Opens a new tkinter window
        res.geometry("622x544")
        photo = PhotoImage(file=r"F:\hassan\winner1.png")
        winner = Label(res, image=photo).place(x=0,y=0)
        winname = Label(res, text=name_1.upper(), fg="gold", bg="#06021a", font=("calibri", 28, "bold", "italic")).place(x=255,y=335)
        Screen().bye()
        res.mainloop()
    elif score_2 == 5:
        windows.ontimer(game_over(), 2000)        # Halts the screen for 2 seconds/2000 milliseconds and runs a function
        res = Toplevel(win)
        res.geometry("622x544")
        photo = PhotoImage(file=r"F:\hassan\winner1.png")
        winner = Label(res, image=photo).place(x=0,y=0)
        winname = Label(res, text=name_2.upper(), fg="gold", bg="#06021a", font=("calibri", 28, "bold", "italic")).place(x=255,y=335)
        Screen().bye()
        res.mainloop()
    Screen().bye()


def twoplayer():                       # Function to ask players to enter their names
    winsound.PlaySound("F:\hassan\selection.wav", winsound.SND_ASYNC)
    global inputname1
    global inputname2
    global pl
    pl = Toplevel(win)
    pl.configure(background="black")
    pl.title("Name Entry")
    inputname1 = StringVar()             # A string variable to hold string data only
    inputname2 = StringVar()
    pl1 = Label(pl, text="Player 1", fg="yellow", bg="black", font=("arial", 20), justify=LEFT).grid(row=0, column=0, padx=10, pady=10)
    pl2 = Label(pl, text="Player 2", fg="yellow",bg="black", font=("arial", 20), justify=LEFT).grid(row=1, column=0, padx=10, pady=10)
    name1 = Entry(pl, width=20, font=("bebas neue", 20, "italic"),fg="white", bg="black", textvariable=inputname1, justify=LEFT)
    name1.grid(row=0, column=1, padx=5, pady=10)
    name2 = Entry(pl, width=20, font=("bebas neue", 20, "italic"), fg="white", bg="black", textvariable=inputname2, justify=LEFT)
    name2.grid(row=1, column=1, padx=5, pady=10)
    start = Button(pl, text="start", fg="black", bg="yellow", bd=3, font=("bebas neue", 20), cursor="hand2", width=8, height=1, command=double).grid(row=2, column=1, padx=10, pady=10)
    pl.mainloop()


#Defining game start menu
win = Tk()
win.title("Start Menu")
win.geometry("570x538")
win.configure(background="black")           # Sets the background colour as you wish
img = PhotoImage(file=r"F:\hassan\pong.png")       # Displaying image
img1 = img.zoom(2,3)
image = Label(win, image=img1).place(x=0, y=0)
name = Label(win, text="BOUNCE!!", fg="lime", bg="black", font=("arial black", 40, "italic")).place(x=160,y=70)
byline = Label(win, text="By TechLord", fg="white", bg="black", font=("arial black", 10, "italic")).place(x=350,y=135)
two_player = Button(win, width=10, text="Play", fg="black", bg="#7fff00", font=("calibri", 20, "bold"), cursor="hand2", command=twoplayer).place(x=230,y=230)
instruct = Button(win, width=10,text="Instructions", fg="black", bg="#7fff00", font=("calibri", 20, "bold"), cursor="hand2", command=instructions).place(x=230,y=300)
about = Button(win, width=10,text="About", fg="black", bg="#7fff00", font=("calibri", 20, "bold"), cursor="hand2", command=About).place(x=230,y=370)
close = Button(win, width=10,text="Exit", fg="black", bg="#7fff00", font=("calibri", 20, "bold"), cursor="hand2", command=Close).place(x=230,y=440)
win.mainloop()

