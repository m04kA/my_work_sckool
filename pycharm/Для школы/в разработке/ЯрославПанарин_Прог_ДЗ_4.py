from tkinter import *
from random import randint
import time

row = int(input('Введите кол. строк: '))
col = int(input('Введите кол. колонок: '))

tk = Tk()
tk.title('Game')
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
tk.wm_attributes('-topmost', 1)


def life(row, col):
    life = []
    for i in range(row):
        life.append([])
        for j in range(col):
            life[i].append(randint(0, 1))
    return life


def board(row, col, life):
    global Dosk
    side = 25
    for i in range(row):
        Dosk.append([])
        for j in range(col):
            Dosk[i].append('*')
            if life[j][i] == 1:
                Dosk[i][j] = canvas.create_rectangle(50 + i * side, 75 + j * side, 50 + side + i * side,
                                                     75 + side + j * side, fill='green')
            else:
                Dosk[i][j] = canvas.create_rectangle(50 + i * side, 75 + j * side, 50 + side + i * side,
                                                     75 + side + j * side, fill='red')


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
        board(row, col, life_for_game)
        tk.update_idletasks()
        tk.update()
        time.sleep(0.025)
        life_is_near = neighor(life_for_game)


def stop_game():
    global stop
    stop = False


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
