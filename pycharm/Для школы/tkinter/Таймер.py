from tkinter import*
import time

tr = False #Для времени
#Время
desatk = 0
edin = 0
dest = 0
sot = 0
color = 'green' # Для покраски


tchk=[[100,191,'Vertikal'],[100,123,'Vertikal'],
      [135,87,'Horizontal'],[170,123,'Vertikal'],
      [170,191,'Vertikal'],[135,227,'Horizontal'],
      [135,157,'Horizontal'],[200,191,'Vertikal'],
      [200,123,'Vertikal'],[235,87,'Horizontal'],
      [270,123,'Vertikal'],[270,191,'Vertikal'],
      [235,227,'Horizontal'],[235,157,'Horizontal'],
      [350,191,'Vertikal'],[350,123,'Vertikal'],
      [385,87,'Horizontal'],[420,123,'Vertikal'],
      [420,191,'Vertikal'],[385,227,'Horizontal'],
      [385,157,'Horizontal'],[450,191,'Vertikal'],
      [450,123,'Vertikal'],[485,87,'Horizontal'],
      [520,123,'Vertikal'],[520,191,'Vertikal'],
      [485,227,'Horizontal'],[485,157,'Horizontal']]
data = [[1,1,1,1,1,1,0],
        [0,0,0,1,1,0,0],
        [1,0,1,1,0,1,1],
        [0,0,1,1,1,1,1],
        [0,1,0,1,1,0,1],
        [0,1,1,0,1,1,1],
        [1,1,1,0,1,1,1],
        [0,0,1,1,1,0,0],
        [1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1]]


def polig(x,y,v_h):
    if v_h=='Horizontal':
        canvas.create_polygon([x-34,y,x-25,y+10,x+25,y+10,x+34,y,x+25,y-10,x-25,y-10],fill=color)
    else:
       canvas.create_polygon([x,y+34,x+10,y+25,x+10,y-25,x,y-34,x-10,y-25,x-10,y+25],fill=color)  

def create(tchk):
    for i in range(28):
        polig(tchk[i][0],tchk[i][1],tchk[i][2])
    wind.update_idletasks()
    wind.update()

def numb(data, edinisa, smeshen, color):
    for i in range(7):
        if data[edinisa][i] == 1:
            canvas.itemconfig(i+smeshen,fill=color)
        else:
            canvas.itemconfig(i+smeshen,fill='black')

def start():
    global desatk
    global edin
    global dest
    global sot
    global color
    global tr
    tr = True
    
    canvas.itemconfig(7,fill='black')
    canvas.itemconfig(14,fill='black')
    canvas.itemconfig(21,fill='black')
    canvas.itemconfig(28,fill='black')
    while 1:
        if tr == True:
            if sot < 9:
                sot += 1
            else:
                sot = 0
                dest += 1
            time.sleep(0.01)
            if dest > 9:
                    dest = 0
                    edin += 1
            if edin > 9:
                    edin = 0
                    desatk += 1
            if desatk > 9:
                    desatk = 0
                    edin = 0
                    dest = 0
                    sot = 0
            numb(data, sot, 22, color)
            wind.update()
            numb(data, dest, 15, color)
            wind.update()
            numb(data, edin, 8, color)
            wind.update()
            numb(data, desatk, 1, color)
            wind.update()
            wind.update_idletasks()
        else:
            break

def stop():
    global tr
    tr = False
def clear():
    global desatk
    global edin
    global dest
    global sot
    global color
    desatk = 0
    edin = 0
    dest = 0
    sot = 0
    for i in range(28):
        canvas.itemconfig(i+1,fill=color)
    wind.update()
    wind.update_idletasks()       
    

def men_col():
    global color
    global tr
    if color == 'green':
        color='red'
        canvas.itemconfig(29,fill='cyan')
        canvas.itemconfig(30,fill='gold')

    else:
        canvas.itemconfig(29,fill='blue')
        canvas.itemconfig(30,fill='purple')                
        color = 'green'
    
    wind.update()
    wind.update_idletasks()       

    
    
    

wind=Tk()
wind.title('Schet')
wind.wm_attributes('-topmost',1)
wind.geometry('600x600+400+200') #Смещение холста
canvas=Canvas(wind,width=600,height=600,bg='black')
canvas.pack()
Start=Button(wind,text='Start',command=start)
Start.place(x=150,y=350)
create(tchk)
canvas.create_rectangle(300,125,325,150,fill='blue')
canvas.create_rectangle(300,175,325,200,fill='purple')

Stop=Button(wind,bg='white',text='Stop',command=stop)
Stop.place(x=200,y=350)

Clear=Button(wind,bg='white',text='Clear',command=clear)
Clear.place(x=250,y=350)

Color=Button(wind,bg='white',text='Change color',command=men_col)
Color.place(x=300,y=350)


            
    
