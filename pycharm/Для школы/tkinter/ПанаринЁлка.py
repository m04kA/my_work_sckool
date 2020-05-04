from tkinter import *
from random import randint
import time
n = int(input('Введите количество строк: '))
label_list = []
a = []
bul = False
bul2 = False
def yellow_Fill():
    for i in range(len(label_list)):
        label_list[i].config(bg = 'yellow')
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())

def qwerty3():
    clean()
    for i in range(len(label_list)):
        label_list[i].config(bg = 'red')
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
       
            

            
def mixx():
    global bul
    def bull():
        global bul
        bul = True
        
    stop = Button(form, text= 'Stop', command = bull)
    stop.place(x = 300, y = 10)

    
    morg = []
    for i in range(len(label_list)):
        if i%3 == 0:
            label_list[i].config(bg = 'red')
            morg.append(i)
        else:
            label_list[i].config(bg = 'purple')
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
    while bul == False:
        
        for i in morg:
            label_list[i].config(bg = 'green')
            if bul == True:
                break
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
        for i in morg:
            label_list[i].config(bg = 'blue')
            if bul == True:
                break            
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
        for i in morg:
            label_list[i].config(bg = 'red')
            if bul == True:
                break            
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
    bul = False
    stop.destroy()
    form.update_idletasks()
    form.update()
    clean()
    form.update_idletasks()
    form.update()
    
            
def qwerty4():
    clean()
    for i in range(len(label_list)):
        if i%2 == 0:
            label_list[i].config(bg = 'purple')
        else:
            label_list[i].config(bg = 'green')
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
    for i in range(len(label_list)):
        if i%2 != 0:
            label_list[i].config(bg = 'purple')
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
       
            

            
def colour_change():
    for i in range(len(label_list)):
        label_list[i].config(bg = 'gold')
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
    for i in range(len(label_list)):
        label_list[i].config(bg = 'purple')
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
    for i in range(len(label_list)):
        label_list[i].config(bg = 'blue')
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
    for i in range(len(label_list)):
        label_list[i].config(bg = 'green')
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())
    
    

def clean():
    for i in range(len(label_list)):
        label_list[i].config(bg = 'green')
        form.update_idletasks()
        form.update()
        time.sleep(0.008)

def reverse():
    clean()
    for i in range(len(label_list)-1, -1, -1):
        label_list[i].config(bg = 'cyan')
        form.update_idletasks()
        form.update()
        time.sleep(scroll.get())


form = Tk()
form.wm_attributes('-topmost', 1)
form.title('Ёлка')
holst = Canvas(form, width=800, height=700)
holst.pack()
scroll = Scale(form, orient = VERTICAL, #ориент.
               length = 280,#длина
               from_ = 0.05, to = 0.55,#от и до
               tickinterval = 0.05,#деление
               resolution = 0.05)
scroll.place(x = 560, y = 30)

knopka1 = Button(form, text= 'Поскучать', command = yellow_Fill)
knopka1.place(x = 30, y = 40)

knopka2 = Button(form, text= 'Бунт програмистов', command = mixx)
knopka2.place(x = 30, y = 90)

knopka3 = Button(form, text= 'Меняем цвет', command = colour_change)
knopka3.place(x = 30, y = 140)

knopka4 = Button(form, text= 'Clear', command = clean)
knopka4.place(x = 30, y = 240)

knopka = Button(form, text = 'Revers', command = reverse)
knopka.place(x = 30, y = 190)


label_list = []
num = 0

for i in range(n): 
    for j in range(0,i+1):
        label_list.append(Label(form, text = '  ', bg = 'green'))
        label_list[num].place(x = 320-(i*15)+(j*30), y = 40+(i*40))
        num+=1
        form.update()
form.update_idletasks()
form.update()
