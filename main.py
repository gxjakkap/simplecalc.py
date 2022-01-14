import tkinter as tk
app = tk.Tk()
app.option_add('*font', 'Ariel 24')
app.title("Calc")
bgcolor = "#C2EABD"
numcolor = "#627264"
opcolor = "#A96DA3"


def clear():
    global expression
    global disp
    result = 0
    expression = ""
    disp.set(result)

def press(item):
    global expression
    expression = expression + str(item)
    disp.set(expression)

def sum():
    global expression
    result = str(eval(expression))
    disp.set(result)
    expression = ""

disp = tk.StringVar()
expression = ""
disp.set(expression)
disp.set(0)

label = tk.Label(app,textvariable=disp, bg=bgcolor, width=22, height=2)
label.grid(row=0, column=0, columnspan=5)
clearb = tk.Button(app, text='C', command=clear, bg="#78C0E0", width=16).grid(row=1, column=0, columnspan=3)
exitb = tk.Button(app, text="OFF", bg=opcolor, command=app.destroy, width=5).grid(row=1, column=3)

sevenb = tk.Button(app,text='7',command=lambda :press('7'), bg=numcolor, width=5).grid(row=2,column=0)
eightb = tk.Button(app,text='8',command=lambda :press('8'), bg=numcolor, width=5).grid(row=2,column=1)
nineb = tk.Button(app,text='9',command=lambda :press('9'), bg=numcolor, width=5).grid(row=2,column=2)
plussb = tk.Button(app,text='+',command=lambda :press('+'), bg=opcolor, width=5).grid(row=2,column=3)

fourb = tk.Button(app,text='4',command=lambda :press('4'), bg=numcolor, width=5).grid(row=3,column=0)
fiveb = tk.Button(app,text='5',command=lambda :press('5'), bg=numcolor, width=5).grid(row=3,column=1)
sixb = tk.Button(app,text='6',command=lambda :press('6'), bg=numcolor, width=5).grid(row=3,column=2)
minusb = tk.Button(app,text='-',command=lambda :press('-'), bg=opcolor, width=5).grid(row=3,column=3)

oneb = tk.Button(app,text='1',command=lambda :press('1'), bg=numcolor, width=5).grid(row=4,column=0)
twob = tk.Button(app,text='2',command=lambda :press('2'), bg=numcolor, width=5).grid(row=4,column=1)
threeb = tk.Button(app,text='3',command=lambda :press('3'), bg=numcolor, width=5).grid(row=4,column=2)
multpb = tk.Button(app,text='x',command=lambda :press('*'), bg=opcolor, width=5).grid(row=4,column=3)

multpb = tk.Button(app,text='÷',command=lambda :press('/'), bg=opcolor, width=5).grid(row=5,column=3)
sumb = tk.Button(app,text='=',command=sum, bg="#78C0E0", width=16).grid(row=5,column=0, columnspan=3)


app.mainloop()