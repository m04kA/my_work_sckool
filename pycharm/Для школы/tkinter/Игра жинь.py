from tkinter import *
from random import randint
import time

row = int(input('Введите кол. строк: '))
col = int(input('Введите кол. колонок: '))

tk = Tk()
tk.title('Game')
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
tk.wm_attributes('-topmost', 1)


def print_tabl(tabl):
    for n in tabl:
        print(' '.join(str(n)))


def life(row, col):
    life = []
    for i in range(row):
        life.append([])
        for j in range(col):
            life[i].append(randint(0, 1))
    return life


def board(row, col, life):
    global Dosk
    side = 15
    for i in range(row):
        Dosk.append([])
        for j in range(col):
            Dosk[i].append('*')
            if life[j][i] == 1:
                Dosk[i][j] = canvas.create_rectangle(50 + i * side, 75 + j * side, 50 + side + i * side,
                                                     75 + side + j * side, fill='green')
            else:
                Dosk[i][j] = canvas.create_rectangle(50 + i * side, 75 + j * side, 50 + side + i * side,
                                                     75 + side + j * side, fill='grey')
    tk.update_idletasks()
    tk.update()


def portrayal(row, col, life):
    count = 1
    global Dosk
    for i in range(row):
        for j in range(col):
            if life[j][i] == 1:
                Dosk[i][j] = canvas.itemconfig(count, fill='green')  # Dosk[i][j]
            else:
                Dosk[i][j] = canvas.itemconfig(count, fill='grey')  # Dosk[i][j]
            count += 1


def neighor(mas):
    score = 0
    spisk = []
    for i in range(len(mas)):
        spisk.append([])
        for j in range(len(mas[0])):
            try:
                if mas[i - 1][j - 1] == 1:
                    score += 1
            except IndexError:
                if (i - 1) >= 0:
                    if mas[i - 1][len(mas[0]) - 1] == 1:
                        score += 1
                elif (j - 1) >= 0:
                    if mas[len(mas) - 1][j - 1] == 1:
                        score += 1
                else:
                    if mas[len(mas) - 1][len(mas[0]) - 1] == 1:
                        score += 1
            try:
                if mas[i - 1][j] == 1:
                    score += 1
            except IndexError:
                if mas[len(mas) - 1][j] == 1:
                    score += 1
            try:
                if mas[i - 1][j + 1] == 1:
                    score += 1
            except IndexError:
                if (i - 1) >= 0:
                    if mas[i - 1][0] == 1:
                        score += 1
                elif (j + 1) <= len(mas[0]) - 1:
                    if mas[len(mas) - 1][j + 1] == 1:
                        score += 1
                else:
                    if mas[len(mas) - 1][0] == 1:
                        score += 1
            try:
                if mas[i][j + 1] == 1:
                    score += 1
            except IndexError:
                if mas[i][0] == 1:
                    score += 1
            try:
                if mas[i + 1][j + 1] == 1:
                    score += 1
            except IndexError:
                if (i + 1) <= len(mas) - 1:
                    if mas[i + 1][len(mas[0]) - j - 1] == 1:
                        score += 1
                elif (j + 1) <= len(mas[0]) - 1:
                    if mas[len(mas) - i - 1][j + 1] == 1:
                        score += 1
                else:
                    if mas[0][0] == 1:
                        score += 1
            try:
                if mas[i + 1][j] == 1:
                    score += 1
            except IndexError:
                if mas[0][j] == 1:
                    score += 1
            try:
                if mas[i + 1][j - 1] == 1:
                    score += 1
            except IndexError:
                if (i + 1) <= len(mas) - 1:
                    if mas[i + 1][len(mas[0]) - 1] == 1:
                        score += 1
                elif (j - 1) >= 0:
                    if mas[0][j - 1] == 1:
                        score += 1
                else:
                    if mas[0][len(mas[0]) - 1] == 1:
                        score += 1
            try:
                if mas[i][j - 1] == 1:
                    score += 1
            except IndexError:
                if mas[i][len(mas[0]) - 1] == 1:
                    score += 1
            spisk[i].append(score)
            score = 0
    return spisk


def print_board(tabl):
    for n in tabl:
        print(' '.join(str(n)))


def game():
    global life_for_game
    global life_is_near
    global Dosk
    global stop
    global first_start
    first_start = True
    stop = True
    while stop == True:
        for i in range(len(life_for_game)):
            for j in range(len(life_for_game[0])):
                if life_for_game[i][j] == 1:
                    if life_is_near[i][j] >= 2 and life_is_near[i][j] <= 3:
                        life_for_game[i][j] = 1
                    else:
                        life_for_game[i][j] = 0
                else:
                    if life_is_near[i][j] == 3:
                        life_for_game[i][j] = 1
                    else:
                        life_for_game[i][j] = 0
        portrayal(row, col, life_for_game)
        life_is_near = neighor(life_for_game)
        # print_tabl(life_for_game)
        # print('----------')
        # print_tabl(life_is_near) #life_is_near
        tk.update_idletasks()
        tk.update()
        time.sleep(0.001)


def stop_game():
    global stop
    stop = False


def Clear():
    global life_for_game
    global life_is_near
    global row, col
    for i in range(row):
        for j in range(col):
            life_for_game[i][j] = 0
            life_is_near[i][j] = 0
    portrayal(row, col, life_for_game)
    life_is_near = neighor(life_for_game)
    tk.update_idletasks()
    tk.update()


def Restart():
    global life_for_game
    global life_is_near
    global row, col
    global Dosk
    global stop

    first_start = False
    stop = False
    life_for_game = life(row, col)
    life_is_near = neighor(life_for_game)
    portrayal(row, col, life_for_game)
    tk.update_idletasks()
    tk.update()


def glider():
    Clear()
    global life_for_game
    global life_is_near
    x = 5
    y = 5
    life_for_game[y][x] = 1
    life_for_game[y + 2][x - 1] = 1
    life_for_game[y + 2][x] = 1
    life_for_game[y + 2][x + 1] = 1
    life_for_game[y + 1][x + 1] = 1
    life_is_near = neighor(life_for_game)
    portrayal(row, col, life_for_game)
    tk.update_idletasks()
    tk.update()
    #game()
def tumber():
    Clear()
    global life_for_game
    global life_is_near
    x = 5
    y = 5
    life_for_game[y][x] = 1
    life_for_game[y][x+1] = 1
    life_for_game[y+1][x] = 1
    life_for_game[y+1][x+1] = 1
    life_for_game[y+2][x+1] = 1
    life_for_game[y+3][x+1] = 1
    life_for_game[y+4][x+1] = 1
    life_for_game[y+5][x] = 1
    life_for_game[y+5][x-1] = 1
    life_for_game[y+4][x-1] = 1
    life_for_game[y+3][x-1] = 1

    life_for_game[y][x+3] = 1
    life_for_game[y][x+4] = 1
    life_for_game[y+1][x+3] = 1
    life_for_game[y+1][x+4] = 1
    life_for_game[y+2][x+3] = 1
    life_for_game[y+3][x+3] = 1
    life_for_game[y+4][x+3] = 1
    life_for_game[y+5][x+4] = 1
    life_for_game[y+5][x+5] = 1
    life_for_game[y+4][x+5] = 1
    life_for_game[y+3][x+5] = 1

    life_is_near = neighor(life_for_game)
    portrayal(row, col, life_for_game)
    tk.update_idletasks()
    tk.update()
    
    
def cross():
    Clear()
    global life_for_game
    global life_is_near
    x = 10
    y = 10
    life_for_game[y][x] = 1
    life_for_game[y-1][x] = 1
    life_for_game[y-2][x] = 1
    life_for_game[y-2][x-1] = 1
    life_for_game[y-2][x-2] = 1
    life_for_game[y-3][x-2] = 1
    life_for_game[y-4][x-2] = 1
    life_for_game[y-5][x-2] = 1
    life_for_game[y-5][x-1] = 1
    life_for_game[y-5][x] = 1
    life_for_game[y-6][x] = 1
    life_for_game[y-7][x] = 1
    life_for_game[y-7][x+1] = 1
    life_for_game[y-7][x+2] = 1
    life_for_game[y-7][x+3] = 1
    life_for_game[y-6][x+3] = 1
    life_for_game[y-5][x+3] = 1
    life_for_game[y-5][x+4] = 1
    life_for_game[y-5][x+5] = 1
    life_for_game[y-4][x+5] = 1
    life_for_game[y-3][x+5] = 1
    life_for_game[y-2][x+5] = 1
    life_for_game[y-2][x+4] = 1
    life_for_game[y-2][x+3] = 1
    life_for_game[y-1][x+3] = 1
    life_for_game[y][x+3] = 1
    life_for_game[y][x+2] = 1
    life_for_game[y][x+1] = 1

    life_is_near = neighor(life_for_game)
    portrayal(row, col, life_for_game)
    tk.update_idletasks()
    tk.update()
    

stop = False
Dosk = []
life_for_game = life(row, col)
board(row, col, life_for_game)
life_is_near = neighor(life_for_game)
# print_board(life_is_near)
start = Button(tk, text='Start', command=game)
start.place(x=0, y=0)

stopping = Button(tk, text='Stop', command=stop_game)
stopping.place(x=0, y=50)

clear = Button(tk, text='Clear', command=Clear)
clear.place(x=50, y=0)

restart = Button(tk, text='Restart', command=Restart)
restart.place(x=50, y=50)

Gider = Button(tk, text='Glider', command=glider)
Gider.place(x=100, y=0)

Tumber = Button(tk, text='Tumber', command=tumber)
Tumber.place(x=150, y=0)

Cross = Button(tk, text='Cross', command=cross)
Cross.place(x=250, y=0)
