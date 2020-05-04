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
Snake = [[8, 4], [7, 4], [6, 4], [5, 4], [4, 4], [3, 4]]
Dosk = []
food = [0, 0]

lv = False
pr = False
dv = False
verh = False


def board(row, col):
    global Dosk
    side = 25
    for i in range(row):
        Dosk.append([])
        for j in range(col):
            Dosk[i].append('*')
            Dosk[i][j] = canvas.create_rectangle(50 + i * side, 75 + j * side, 50 + side + i * side,75 + side + j * side, fill='dark green')


def zmeya():
    for i in range(len(Snake)):
        if i == 0:
            canvas.itemconfig(Dosk[Snake[i][0]][Snake[i][1]], fill='red')
        else:
            canvas.itemconfig(Dosk[Snake[i][0]][Snake[i][1]], fill='blue')


def right(evt):
    global pr
    global lv
    global dv
    global verh
    global food
    lv = False
    dv = False
    verh = False
    pr = True
    while pr == True:
        if Snake[0][0] < len(Dosk) - 1:
            Snake.insert(0, [Snake[0][0] + 1, Snake[0][1]])
            canvas.itemconfig(Dosk[Snake[0][0]][Snake[0][1]], fill='red')
            canvas.itemconfig(Dosk[Snake[1][0]][Snake[1][1]], fill='blue')
            if Snake[0][0] == food[0] and Snake[0][1] == food[1]:
                canvas.itemconfig(Dosk[food[0]][food[1]], fill='red')
                food = [randint(0, len(Dosk) - 1), randint(0, len(Dosk[0]) - 1)]
                canvas.itemconfig(Dosk[food[0]][food[1]], fill='orange')
                score.config(text = score['text'][:6] + str(int(score['text'][6:])+1))
            else:
                canvas.itemconfig(Dosk[Snake[len(Snake) - 1][0]][Snake[len(Snake) - 1][1]], fill='dark green')
                del Snake[len(Snake) - 1]
            tk.update()
            tk.update_idletasks()
            
        else:
            lv = False
            pr = False
            dv = False
            verh = False
            
            '''
            canvas.delete("all")
            text = Label(tk, text='GAME OVER', bg='red')  # Текст (просто текст в форме)
            text.place(300, 300)
            time.sleep(5)
            exit()
            '''
        time.sleep(0.5)


def dovn(evt):
    global pr
    global lv
    global dv
    global verh
    global food
    lv = False
    verh = False
    pr = False
    dv = True
    while dv == True:
        if Snake[0][1] < len(Dosk[0]) - 1:
            Snake.insert(0, [Snake[0][0], Snake[0][1] + 1])
            canvas.itemconfig(Dosk[Snake[0][0]][Snake[0][1]], fill='red')
            canvas.itemconfig(Dosk[Snake[1][0]][Snake[1][1]], fill='blue')
            if Snake[0][0] == food[0] and Snake[0][1] == food[1]:
                canvas.itemconfig(Dosk[food[0]][food[1]], fill='red')
                food = [randint(0, len(Dosk) - 1), randint(0, len(Dosk[0]) - 1)]
                canvas.itemconfig(Dosk[food[0]][food[1]], fill='orange')
                score.config(text = score['text'][:6] + str(int(score['text'][6:])+1))
            else:
                canvas.itemconfig(Dosk[Snake[len(Snake) - 1][0]][Snake[len(Snake) - 1][1]], fill='dark green')
                del Snake[len(Snake) - 1]
            tk.update()
            tk.update_idletasks()
            
        else:
            lv = False
            pr = False
            dv = False
            verh = False
            
            '''
            canvas.delete("all")
            text = Label(tk, text='GAME OVER', bg='red')  # Текст (просто текст в форме)
            text.place(300, 300)
            time.sleep(5)
            exit()
            '''
        time.sleep(0.5)


def left(evt):
    global pr
    global lv
    global dv
    global verh
    global food
    lv = True
    dv = False
    verh = False
    pr = False
    while lv == True:
        if Snake[0][0] > 0:
            Snake.insert(0, [Snake[0][0] - 1, Snake[0][1]])
            canvas.itemconfig(Dosk[Snake[0][0]][Snake[0][1]], fill='red')
            canvas.itemconfig(Dosk[Snake[1][0]][Snake[1][1]], fill='blue')
            if Snake[0][0] == food[0] and Snake[0][1] == food[1]:
                canvas.itemconfig(Dosk[food[0]][food[1]], fill='red')
                food = [randint(0, len(Dosk) - 1), randint(0, len(Dosk[0]) - 1)]
                canvas.itemconfig(Dosk[food[0]][food[1]], fill='orange')
                score.config(text = score['text'][:6] + str(int(score['text'][6:])+1))
            else:
                canvas.itemconfig(Dosk[Snake[len(Snake) - 1][0]][Snake[len(Snake) - 1][1]], fill='dark green')
                del Snake[len(Snake) - 1]
            tk.update()
            tk.update_idletasks()
            
        else:
            lv = False
            pr = False
            dv = False
            verh = False
            
            '''
            canvas.delete("all")
            text = Label(tk, text='GAME OVER', bg='red')  # Текст (просто текст в форме)
            text.place(300, 300)
            time.sleep(5)
            exit()
            '''
        time.sleep(0.5)


def up(evt):
    global pr
    global lv
    global dv
    global verh
    global food
    lv = False
    dv = False
    pr = False
    verh = True
    while verh == True:
        if Snake[0][1] > 0:
            Snake.insert(0, [Snake[0][0], Snake[0][1] - 1])
            canvas.itemconfig(Dosk[Snake[0][0]][Snake[0][1]], fill='red')
            canvas.itemconfig(Dosk[Snake[1][0]][Snake[1][1]], fill='blue')
            if Snake[0][0] == food[0] and Snake[0][1] == food[1]:
                canvas.itemconfig(Dosk[food[0]][food[1]], fill='red')
                food = [randint(0, len(Dosk) - 1), randint(0, len(Dosk[0]) - 1)]
                canvas.itemconfig(Dosk[food[0]][food[1]], fill='orange')
                score.config(text = score['text'][:6] + str(int(score['text'][6:])+1))
            else:
                canvas.itemconfig(Dosk[Snake[len(Snake) - 1][0]][Snake[len(Snake) - 1][1]], fill='dark green')
                del Snake[len(Snake) - 1]
            tk.update()
            tk.update_idletasks()
            
        else:
            lv = False
            pr = False
            dv = False
            verh = False

            '''
            canvas.delete("all")
            text = Label(tk, text='GAME OVER', bg='red')  # Текст (просто текст в форме)
            text.pack()
            time.sleep(5)
            exit()
        '''
        time.sleep(0.5)


board(row, col)
zmeya()
score =Label(tk, text = 'Счёт: 0', relief="solid",highlightthickness = 2)
score.pack()
canvas.itemconfig(Dosk[food[0]][food[1]], fill='orange')
canvas.bind_all('<KeyPress-Left>', left)
canvas.bind_all('<KeyPress-Up>', up)
canvas.bind_all('<KeyPress-Down>', dovn)
canvas.bind_all('<KeyPress-Right>', right)
