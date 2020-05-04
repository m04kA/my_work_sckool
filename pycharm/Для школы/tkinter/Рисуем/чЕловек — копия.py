from tkinter import *
import time

#img = PhotoImage(file = 'bg.png')
#img2 = PhotoImage(file = 'bg2.png')

class Man:
    def __init__(self,canvas):#два нижних подчёркивания!!!
        self.img = [PhotoImage(file = 'bg.png'), PhotoImage(file = 'bg2.png')]
        #self.img2 = PhotoImage(file = 'bg2.png')
        self.canvas = canvas
        self.id = canvas.create_image(250, 250, image = self.img[0])
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('a',self.turn_left)
        self.canvas.bind_all('d',self.turn_right)
    def turn_left(self,evt):
        if self.pos[0] >=2:
            self.x = -3
    def turn_right(self,evt):
        if self.pos[2] <=self.canvas_width-2:
            self.x = 3

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        self.pos = self.canvas.coords(self.id)
        if self.pos[0] <=0:
            self.x = 0
        elif self.pos[2] >= self.canvas_width:
            self.x = 0


#def opa(evt):
#    popal = canvas.create_image(250, 250, image = img)
#    canvas.move(popal, 5, 0)
#tk.bind('w', opa)



        
tk = Tk()
tk.title('begi poka molodoy')
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk, width = 500, heigh = 500, bd = 0)
canvas.pack()#Упаковываем

img3= PhotoImage( file = 'ban.png')
for i in range(5):
    for j in range(5):
        canvas.create_image(50+i*100, 50+j*100, image = img3)
men = Man(canvas)
while 1 :
    men.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)    


