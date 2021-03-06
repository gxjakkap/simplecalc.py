import tkinter as tk
#import math
app = tk.Tk()
app.option_add('*font', 'Ariel 24')
app.title("Simplecalc.py")
bgcolor = "#C2EABD"
numcolor = "#627264"
opcolor = "#A96DA3"
funccolor = "#78C0E0"
required_symbols = ['+', '-', '*', '/']
allowed_symbols = ['0', '1', '2', '3', '4', '5',' 6', '7', '8', '9', '+', '-', '*', '/', '.']


def clear():
    global expression
    global disp
    result = 0
    expression = "0"
    disp.set(result)

def rem():
    global expression
    global disp
    if len(expression)==1 and expression=="0":
        return
    elif len(expression)==1:
        expression = "0"
        disp.set(expression)
    else:
        expression = expression[:-1]
        disp.set(expression)

def press(item):
    global expression
    expression = expression + str(item)
    if expression[0] == "0" and len(expression)==2 and item not in required_symbols:
        expression = expression[-1:]
    disp.set(expression)

def presskey(event):
    global expression
    item = event.char
    if item not in allowed_symbols:
        print(item, event)
        if event.keysym == "equal" or event.keysym == 'Return' or event.keysym == "KP_Enter" or event.keysym == "KP_Equal":
            sum()
            return
        elif event.keysym == "BackSpace":
            rem()
            return
        elif event.keysym == "Delete":
            clear()
            return
        else:
            return    
    expression = expression + str(item)
    if expression[0] == "0" and len(expression)==2 and item not in required_symbols:
        expression = expression[-1:]
    disp.set(expression)


def sum():
    global expression
    global required_symbols
    x = any(expression in required_symbols for expression in expression)
    if not x:
        return
    try:
        result = str(eval(expression))
        disp.set(result)
        expression = result
    except Exception as error: 
        disp.set(error)
        expression = "0"

def key_init():
    clearb = tk.Button(app, text='Clear', command=clear, bg=funccolor, width=16).grid(row=1, column=0, columnspan=3)
    exitb = tk.Button(app, text="???", bg=funccolor, command=rem, width=5).grid(row=1, column=3)
    #exitb = tk.Button(app, text="OFF", bg=opcolor, command=app.destroy, width=5).grid(row=1, column=3)

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

    divb = tk.Button(app,text='??',command=lambda :press('/'), bg=opcolor, width=5).grid(row=5,column=3)
    zerob = tk.Button(app,text='0',command=lambda: press('0'), bg=funccolor, width=5).grid(row=5,column=0)
    symb = tk.Button(app,text='.',command=lambda: press('.'), bg=funccolor, width=5).grid(row=5,column=1)
    sumb = tk.Button(app,text='=',command=sum, bg=funccolor, width=5).grid(row=5,column=2)    

disp = tk.StringVar()
expression = "0"
disp.set(expression)
label = tk.Label(app,textvariable=disp, bg=bgcolor, width=22, height=2)
label.grid(row=0, column=0, columnspan=5)
key_init()
app.bind('<Key>', presskey)
app.mainloop()