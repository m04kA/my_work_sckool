from tkinter import *
import time
from random import randint
#с пом self в классе все функции связаны между собой
#классы можно исп для одного типа объектов
class Ball:
    def __init__(self, canvas, color, speed_x, speed_y, cent_x, cent_y): #paddle):
        self.canvas = canvas
        #self.paddle = paddle
        self.centr_x = cent_x
        self.centr_y = cent_y
        self.id=canvas.create_oval(10,10,30,30, fill = color)#создали пр-к
        self.canvas.move(self.id,self.centr_x,self.centr_y)#передвинули пр-к
        self.canvas_width = self.canvas.winfo_width()
        self.x = speed_x
        self.y = speed_y
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        self.coords = self.canvas.coords(self.id)
        if self.coords[0]<=0:
            self.x = -self.x
        if self.coords[1] <=0:
            self.y = -self.y
        if self.coords[2] >= self.canvas_width:
            self.x = -self.x
        if self.coords[3] >= 500:#self.canvas_heigth:
            self.y = -self.y
    #     if self.hit_paddle(self.coords) == True:
    #         self.y = -self.y
    #         score.config(text = score['text'][:6] + str(int(score['text'][6:])+1))
    # def hit_paddle(self,coords):
    #     paddle_coords = self.canvas.coords(self.paddle.id)
    #     if coords[2] >= paddle_coords[0] and coords[0] <= paddle_coords[2]:
    #         if coords[3]>= paddle_coords[1] and coords[3]<=paddle_coords[3]:
    #             return True
    #     return False


class Paddle:#класс ракетки
    def __init__(self,canvas,color):#два нижних подчёркивания!!!
        self.canvas = canvas
        self.id=canvas.create_rectangle(0,0,100,10, fill = color)#создали пр-к
        #self.id2 = canvas.create_rectangle(000,0,10,20, fill = color)
        self.canvas.move(self.id,400,400)#передвинули пр-к
        self.x = 0 #скорость дв-я в нач. момент = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def turn_left(self,evt):
        if self.coords[0]>=2:
            self.x = -5
    def turn_right(self,evt):
        if self.coords[2] <=self.canvas_width-2:
            self.x = 5
    def draw(self):#отрисовываем
        self.canvas.move(self.id,self.x,0)
        self.coords = self.canvas.coords(self.id)
        if self.coords[0]<=0:
            self.x = 0
        elif self.coords[1] <= 0:
            self.y = -self.y
        elif self.coords[2] >= self.canvas_width:
            self.x = 0

def stolk(ball_1, ball_2):
    if ball_1.coords[0] > ball_2.coords[0] and ball_1.coords[0] < ball_2.coords[2] or ball_1.coords[2] > ball_2.coords[0] and ball_1.coords[2] < ball_2.coords[2] or ball_2.coords[0] > ball_1.coords[0] and ball_2.coords[0] < ball_1.coords[2] or ball_2.coords[2] > ball_1.coords[0] and ball_2.coords[2] < ball_1.coords[2]:
        return True
    else:
        return False

def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0

def speed_bals(ball_1, ball_2):
    zn_1 = sign(ball_1.x)
    zn_2 =sign(ball_2.x)
    sp_1 = ball_1.x
    sp_2 = ball_2.x
    if (zn_1 == 1 and zn_2 == -1) or (zn_1 == -1 and zn_2 == 1):
        speed = (abs(sp_1) + abs(sp_2))/2
        sp_1 = speed * zn_2
        sp_2 = speed * zn_1
    else:
        if sp_1 > sp_2:
            sp_2 = zn_1*((abs(sp_1) + abs(sp_2))/3)
            sp_1 = 0
        else:
            sp_1 = zn_2*((abs(sp_1) + abs(sp_2)) / 3)
            sp_2 = 0
    return sp_1, sp_2


def collg(ball_1, ball_2):
    if stolk(ball_1, ball_2) == True:
        ball_1.x, ball_2.x = speed_bals(ball_1, ball_2)

tk = Tk()
tk.title('asdasd')
tk.wm_attributes('-topmost',1)#закрепление экрана поверх других окон
canvas = Canvas(tk, width = 600, heigh = 500, bd = 0, highlightthickness = 0)
canvas.pack()#Упаковываем
#score =Label(tk, text = 'Счёт: 0', relief="solid",highlightthickness = 2)
#score.place(x=50,y=30)
tk.update()#Обновление экрана
#paddle = Paddle(canvas, 'red')
ball_1 = Ball(canvas, 'blue', -2, 0, 140, 50)#, paddle)
ball_2 = Ball(canvas, 'green', -5, 0, 100, 50)#, paddle)
while 1:#запускаем бесконечный цикл
    #paddle.draw()
    ball_1.draw()
    ball_2.draw()
    collg(ball_1, ball_2)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
