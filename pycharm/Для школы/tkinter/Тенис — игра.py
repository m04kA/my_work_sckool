from tkinter import *
import time
from random import randint
#с пом self в классе все функции связаны между собой
#классы можно исп для одного типа объектов
class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id=canvas.create_oval(10,10,30,30, fill = color)#создали пр-к
        self.canvas.move(self.id,randint(50,450),50)#передвинули пр-к
        self.canvas_width = self.canvas.winfo_width()
        self.x = -4
        self.y = -4
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        self.pos = self.canvas.coords(self.id)
        if self.pos[0]<=0:
            self.x = -self.x
        if self.pos[1] <=0:
            self.y = -self.y
        if self.pos[2] >= self.canvas_width:
            self.x = -self.x
        if self.pos[3] >= 500:#self.canvas_heigth:
            self.y = -self.y
        if self.hit_paddle(self.pos) == True:
            self.y = -self.y
            score.config(text = score['text'][:6] + str(int(score['text'][6:])+1))
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3]>= paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False


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
        if self.pos[0]>=2:
            self.x = -5
    def turn_right(self,evt):
        if self.pos[2] <=self.canvas_width-2:
            self.x = 5
    def draw(self):#отрисовываем
        self.canvas.move(self.id,self.x,0)
        self.pos = self.canvas.coords(self.id)
        if self.pos[0]<=0:
            self.x = 0
        elif self.pos[1] <= 0:
            self.y = -self.y
        elif self.pos[2] >= self.canvas_width:
            self.x = 0


tk = Tk()
tk.title('asdasd')
tk.resizable(0,0)#?
tk.wm_attributes('-topmost',1)#закрепление экрана поверх других окон
canvas = Canvas(tk, width = 600, heigh = 500, bd = 0, highlightthickness = 0)
canvas.pack()#Упаковываем
score =Label(tk, text = 'Счёт: 0', relief="solid",highlightthickness = 2)
score.place(x=50,y=30)
tk.update()#Обновление экрана
paddle = Paddle(canvas, 'red')
ball_1 = Ball(canvas, 'blue', paddle)
ball_2 = Ball(canvas, 'green', paddle)
while 1:#запускаем бесконечный цикл
    paddle.draw()
    ball_1.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
