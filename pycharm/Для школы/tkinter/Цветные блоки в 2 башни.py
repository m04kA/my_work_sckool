from tkinter import *
tk=Tk()
tk.title('window')
canvas=Canvas(tk,width=400,height=400)
canvas.pack()
first = 0
second = 0
block = []

def red(evt):
    global first
    global second
    global block
    if first < 12:
        block.append(canvas.create_rectangle(50,150-first*11,90,140-first*11,fill='red'))
        first += 1
        
    else:
        if second < 12:
            block.append(canvas.create_rectangle(150,150-second*11,190,140-second*11,fill='red'))
            second += 1
def green(evt):
    global first
    global second
    global block
    if first < 12:
        block.append(canvas.create_rectangle(50,150-first*11,90,140-first*11,fill='green'))
        first += 1
        
    else:
        if second < 12:
            block.append(canvas.create_rectangle(150,150-second*11,190,140-second*11,fill='green'))
            second += 1

def blue(evt):
    global first
    global second
    global block
    if first < 12:
        block.append(canvas.create_rectangle(50,150-first*11,90,140-first*11,fill='blue'))
        first += 1
        
    else:
        if second < 12:
            block.append(canvas.create_rectangle(150,150-second*11,190,140-second*11,fill='blue'))
            second += 1

def back(evt):
    global first
    global second
    global block

    if block != []:
        el = block.pop() #del last el
        canvas.delete(el)

        if second != 0:
            second -= 1
        elif first != 0:
            first -= 1
    


canvas.bind_all('<r>',red)
canvas.bind_all('<g>',green)
canvas.bind_all('<b>',blue)
canvas.bind_all('<z>',back)
