from tkinter import *
from random import randint
import time

def summ1():
        global multi
        if multi['text'] == '0':
                multi.config(text = str(1))
        else:
                multi.config(text = str(multi['text']) + '1')
        okno.update_idletasks()
        okno.update()

def summ2():
        global multi
        if multi['text'] == '0':
                multi.config(text = str(2))
        else:
                multi.config(text = str(multi['text']) + '2')
        okno.update_idletasks()
        okno.update()

def summ3():
        global multi
        if multi['text'] == '0':
                multi.config(text = str(3))
        else:
                multi.config(text = str(multi['text']) + '3')
        okno.update_idletasks()
        okno.update()

def summ4():
        global multi
        if multi['text'] == '0':
                multi.config(text = str(4))
        else:
                multi.config(text = str(multi['text']) + '4')
        okno.update_idletasks()
        okno.update()

def summ5():
        global multi
        if multi['text'] == '0':
                multi.config(text = str(5))
        else:
                multi.config(text = str(multi['text']) + '5')
        okno.update_idletasks()
        okno.update()

def summ6():
        global multi
        if multi['text'] == '0':
                multi.config(text = str(6))
        else:
                multi.config(text = str(multi['text']) + '6')
        okno.update_idletasks()
        okno.update()

def summ7():
        global multi
        if multi['text'] == '0':
                answ.config(text = str(7))
        else:
                multi.config(text = str(multi['text']) + '7')
        okno.update_idletasks()
        okno.update()

def summ8():
        global multi
        if multi['text'] == '0':
                multi.config(text = str(8))
        else:
                multi.config(text = str(multi['text']) + '8')
        okno.update_idletasks()
        okno.update()

def summ9():
        global multi
        if multi['text'] == '0':
                multi.config(text = str(9))
        else:
                multi.config(text = str(multi['text']) + '9')
        okno.update_idletasks()
        okno.update()

def summ0():
        global multi
        if multi['text'] == '0':
                multi.config(text = str(0))
        else:
                multi.config(text = str(multi['text']) + '0')
        okno.update_idletasks()
        okno.update()

def plus():
        global multi
        multi.config(text = str(multi['text']) + ' + ')
        okno.update_idletasks()
        okno.update()

def minus():
        global multi
        multi.config(text = str(multi['text']) + ' - ')
        okno.update_idletasks()
        okno.update()

def ymno():
        global multi
        multi.config(text = str(multi['text']) + ' * ')
        okno.update_idletasks()
        okno.update()

def delit():
        global multi
        multi.config(text = str(multi['text']) + ' / ')
        okno.update_idletasks()
        okno.update()

def reset():
        global multi
        global score
        multi.config(text = str(0))
        answ.config(text = str(0))
        score = 0
        okno.update_idletasks()
        okno.update()

def ravn():
        global answ
        global multi
        global score
        if score == 0:
                viraj = multi['text'].split()
                if str(viraj[1]) == '+':
                        multi.config(text = str(int(viraj[0])) + str(' ' +viraj[1] + ' ') + str(viraj[2]) + ' =')
                        answ.config(text = str(int(viraj[0]) + int(viraj[2])))
                elif str(viraj[1]) == '-':
                        multi.config(text = str(int(viraj[0])) + str(' ' +viraj[1] + ' ') + str(viraj[2]) + ' =')
                        answ.config(text = str(int(viraj[0]) - int(viraj[2])))
                elif str(viraj[1]) == '/':
                        multi.config(text = str(int(viraj[0])) + str(' ' +viraj[1] + ' ') + str(viraj[2]) + ' =')
                        answ.config(text = str(int(viraj[0]) / int(viraj[2])))
                elif str(viraj[1]) == '*':
                        multi.config(text = str(int(viraj[0])) + str(' ' +viraj[1] + ' ') + str(viraj[2]) + ' =')
                        answ.config(text = str(int(viraj[0]) * int(viraj[2])))
               # answ.config(text = str(int(viraj[0]) + int(viraj[2])))
                okno.update_idletasks()
                okno.update()
                score += 1
        else:
                viraj = multi['text'].split()
                viraj[0] = int(float(answ['text']))
                if str(viraj[1]) == '+':
                        multi.config(text = str(answ['text']) + str(' ' +viraj[1] + ' ') + str(viraj[2]) + ' =')
                        answ.config(text = str(int(viraj[0]) + int(viraj[2])))
                elif str(viraj[1]) == '-':
                        multi.config(text = str(answ['text']) + str(' ' +viraj[1] + ' ') + str(viraj[2]) + ' =')
                        answ.config(text = str(int(viraj[0]) - int(viraj[2])))
                elif str(viraj[1]) == '/':
                        viraj[0] = float(answ['text'])
                        multi.config(text = str(answ['text']) + str(' ' +viraj[1] + ' ') + str(viraj[2]) + ' =')
                        answ.config(text = str(float(viraj[0]) / float(viraj[2])))
                elif str(viraj[1]) == '*':
                        multi.config(text = str(answ['text']) + str(' ' +viraj[1] + ' ') + str(viraj[2]) + ' =')
                        answ.config(text = str(int(viraj[0]) * int(viraj[2])))
                okno.update_idletasks()
                okno.update()
                score += 1
                
                
        
        
     
okno = Tk()
okno.wm_attributes('-topmost', 1)
okno.title('Окошко')

holst = Canvas(okno, width=600, height=400)
holst.pack()

one = Button(okno, text= '1',font = "GOST 20", command = summ1)
one.place(x = 30, y = 100)

two = Button(okno, text= '2',font = "GOST 20", command = summ2)
two.place(x = 120, y = 100)

three = Button(okno, text= '3',font = "GOST 20", command = summ3)
three.place(x = 210, y = 100)

fore = Button(okno, text= '4',font = "GOST 20", command = summ4)
fore.place(x = 30, y = 170)

five = Button(okno, text= '5',font = "GOST 20", command = summ5)
five.place(x = 120, y = 170)

six = Button(okno, text= '6',font = "GOST 20", command = summ6)
six.place(x = 210, y = 170)

sew = Button(okno, text= '7',font = "GOST 20", command = summ7)
sew.place(x = 30, y = 240)

eigh = Button(okno, text= '8',font = "GOST 20", command = summ8)
eigh.place(x = 120, y = 240)

nine = Button(okno, text= '9',font = "GOST 20", command = summ9)
nine.place(x = 210, y = 240)

zir = Button(okno, text= '0',font = "GOST 20", command = summ0)
zir.place(x = 120, y = 310)

plus = Button(okno, text= '+',font = "GOST 20", command = plus)
plus.place(x = 310, y = 100)

minus = Button(okno, text= '-',font = "GOST 20", command = minus)
minus.place(x = 310, y = 170)

ymno = Button(okno, text= '*',font = "GOST 20", command = ymno)
ymno.place(x = 310, y = 240)

delit = Button(okno, text= '/',font = "GOST 20", command = delit)
delit.place(x = 310, y = 310)

reset = Button(okno, text= 'res',font = "GOST 20", command = reset)
reset.place(x = 30, y = 310)

ravn = Button(okno, text= '=',font = "GOST 20", command = ravn)
ravn.place(x = 210, y = 310)

multi = Label(okno, text = str(0))
multi.place(x=20, y = 20)
answ = Label(okno)
answ.place(x=20,y=50)
score = 0

#while len(answ['text'].split())%2 != 0:
        
