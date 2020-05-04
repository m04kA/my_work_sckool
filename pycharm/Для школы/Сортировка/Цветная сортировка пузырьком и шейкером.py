from tkinter import *
import time
from random import randint

form = Tk() #Создание формы для работы
form.wm_attributes('-topmost',1)
form.title('Сортировка пузырьком')    #Переименование формы

holst1 = Canvas(form, width=400, height=400)  #Созданием холста где мы всё размещаем
holst1.pack()
long = int(input('Введите длинну одномерного массива: '))



def bubble():
    global mass
    for i in range(len(mass)-1):
        for j in range(len(mass)-1-i):
            mass[j].config(bg = 'yellow')
            mass[j+1].config(bg = 'yellow')
            form.update_idletasks()
            if int(mass[j]['text']) > int(mass[j+1]['text']):
                time.sleep(0.5)
                mass[j]['text'],mass[j+1]['text'] = mass[j+1]['text'],mass[j]['text']
                form.update_idletasks()
                form.update()
            time.sleep(0.5)
            mass[j].config(bg = 'grey')
            mass[j+1].config(bg = 'grey')
            form.update_idletasks()
            form.update()
            time.sleep(0.5)
        mass[len(mass)-1-i].config(bg = 'green')
        form.update_idletasks()
        form.update()
    mass[0].config(bg = 'green')
    form.update_idletasks()
    form.update()


def sheyker():
    global sor
    left = 0              #Переменная для движения с права на лева
    right = len(sor)-1 #Переменная для движения с лева на права

    while left <= right:
        for i in range(left,right,1):                      #Самый тяжёлый элемент в право
            sor[i].config(bg = 'red')
            sor[i+1].config(bg = 'red')
            form.update_idletasks()
            time.sleep(0.5)
            if int(sor[i]['text']) > int(sor[i+1]['text']):
                sor[i]['text'],sor[i+1]['text'] = sor[i+1]['text'],sor[i]['text']
                form.update_idletasks()
                time.sleep(0.5)
                sor[i].config(bg = 'purple')
                sor[i+1].config(bg = 'purple')
                form.update_idletasks()
            sor[i].config(bg = 'purple')
            sor[i+1].config(bg = 'purple')
            form.update_idletasks()
            form.update()
            time.sleep(0.5)

        sor[right].config(bg = 'green')
        form.update_idletasks()
        form.update()
        
        right -=1                                   #Пропускаем самый большой элемент, который уже занял своё место

        for i in range(right,left,-1):              #Самый лёгкий элемент в лево
            sor[i].config(bg = 'red')
            sor[i-1].config(bg = 'red')
            form.update_idletasks()
            form.update()
            time.sleep(0.5)
            if int(sor[i]['text']) < int(sor[i-1]['text']):
                sor[i]['text'],sor[i-1]['text'] = sor[i-1]['text'],sor[i]['text']
                form.update_idletasks()
                form.update()
                time.sleep(0.5)
                sor[i].config(bg = 'purple')
                sor[i-1].config(bg = 'purple')
                form.update_idletasks()
                form.update()
            sor[i].config(bg = 'purple')
            sor[i-1].config(bg = 'purple')
            form.update_idletasks()
            form.update()
            time.sleep(0.5)
        sor[left].config(bg = 'green')
        left +=1
        form.update_idletasks()
        form.update()
                                            #Пропускаем самый лёгкий элемент, занявший своё место



start_bubble = Button(form, text='Start bubble', command = bubble)
start_bubble.place(x = 100, y = 100) #Размещение кнопки по координатам

start_sheyker = Button(form, text='Start sheyker', command = sheyker)
start_sheyker.place(x = 200, y = 100) #Размещение кнопки по координатам



text = Label(form, text = 'Y.P.', bg = 'red') #Текст (просто текст в форме)
text.pack()


mass = [] #Для bubble
sor = [] #Для sheyker
for i in range(long):
    mass.append(Label(form, text = str(randint(1,100)), bg = 'grey'))
    sor.append(Label(form, text = str(randint(1,100)), bg = 'purple'))
    mass[i].place(x = 30*(i+1), y = 20)
    sor[i].place(x = 30*(i+1), y = 60)
form.update_idletasks()
#for i in range(10):
#    mass[i].config( text = str(i+2), bg = 'red')
 #   time.sleep(0.5)
  #  form.update_idletasks()
   # form.update()





