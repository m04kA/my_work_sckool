from tkinter import *

tk = Tk()
tk.title('asdasd')
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk, width = 500, heigh = 500, bd = 0)
canvas.pack()#Упаковываем
img = PhotoImage(file = 'bg.png')
img2 = PhotoImage(file = 'bg2.png')
img3 = PhotoImage(file = 'ban.png')

mape = [[0,1,0,0,0],
               [0,0,0,0,1],
               [0,0,1,0,0],
               [0,1,0,0,0],
               [0,0,0,1,0]]

for i in range(5):
    for j in range(5):
        if mape[i][j] == 1:
            canvas.create_image(50+i*100, 50+j*100, image = img)
        else:
            canvas.create_image(50+i*100, 50+j*100, image = img2)
        tk.update()
def opa(evt):
    popal = canvas.create_image(250, 250, image = img3)
    canvas.move(popal, 5, 0)
tk.bind('w', opa)

