from tkinter import *
import tkinter.font as font
from tkinter import ttk

root = Tk()
root.title("Volume Converter App")
root.geometry("600x700+300+10")
root.configure(background='#CEE5E1')

font1 = font.Font(family='helvetica', size='30')
font2 = font.Font(family='helvetica', size='20')

def fromfunc(event):
    global result_from
    result_from = event.widget.get()

def tofunc(event):
    global result_to
    result_to = event.widget.get()

def convert():
    try:
        number1 = float(ent_num.get())  
        
        if number1 < 0:
            result.configure(text="Input cannot be negative")
            ent_num.delete(0, END)
            ent_num.focus()
            return
        
        if result_from == 'Liters' and result_to == 'Gallons':
            calculate = number1 * 0.26417
            result.configure(text=f"{calculate:.2f} {result_to}")
        elif result_from == 'Gallons' and result_to == 'Liters':
            calculate = number1 * 3.7854
            result.configure(text=f"{calculate:.2f} {result_to}")
        ent_num.delete(0, END)
        ent_num.focus()
    except ValueError:
        result.configure(text="Invalid input")
        ent_num.delete(0, END)
        ent_num.focus()

def selected(event):
    unit = event.widget.get()
    if unit == 'Volume':
        fromdd['values'] = ('Liters', 'Gallons')
        todd['values'] = ('Liters', 'Gallons')

label_msg = Label(root, text='Volume Converter', bg='#CEE5E1')
label_msg['font'] = font1
label_msg.place(x=150, y=20)

unit = Label(root, text='Unit -:', bg='#CEE5E1')
unit['font'] = font2
unit.place(x=50, y=110)

n = StringVar()
unitdd = ttk.Combobox(root, width='45', state="readonly", textvariable=n)
unitdd['values'] = ('Volume')
unitdd.place(x=150, y=120)
unitdd.bind('<<ComboboxSelected>>', selected)

label_from = Label(root, text='From -:', bg='#CEE5E1')
label_from['font'] = font2
label_from.place(x=50, y=200)

f = StringVar()
fromdd = ttk.Combobox(root, width='45', state="readonly", textvariable=f)
fromdd.place(x=150, y=210)
fromdd.bind('<<ComboboxSelected>>', fromfunc)

to = Label(root, text='To -:', bg='#CEE5E1')
to['font'] = font2
to.place(x=50, y=300)

t = StringVar()
todd = ttk.Combobox(root, width=45, state="readonly", textvariable=t)
todd.place(x=150, y=310)
todd.bind('<<ComboboxSelected>>', tofunc)

lab_num = Label(root, text="Enter Num :", font=font2, bg='#CEE5E1')
lab_num.place(x=30, y=400)
ent_num = Entry(root, font=font2)
ent_num.place(x=200, y=400)

result = Label(root, text='', bg='white', width=25)
result['font'] = font2
result.place(x=100, y=500)

get_answer = Button(root, text='Get Answer', command=convert)
get_answer['font'] = font2
get_answer.place(x=200, y=580)

root.mainloop()