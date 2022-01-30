#this is contribution
from tkinter import *
from tkinter import  messagebox
prev = ''
value = ''
play_1 : list
play_2 :list
def func(x):
    global prev
    global value
    color = ''
    if prev == '' or prev == 'O':
        value = 'X'
        prev = 'X'
        color = 'red'
    else:
        value = 'O'
        prev = 'O'
        color = 'blue'
    
    if x['text'] == '':
        x.config(text = value,background = color,state = 'disable',fg = 'green')
    result()
def update():
    global value
    value = ''
    btn= 0
    for x in range(3):
        for y in range(3):
            button[btn].config(text = value,background = 'SystemButtonFace',state = 'normal')
            btn+=1
def result():
    button = [[btn1,btn2,btn3],[btn4,btn5,btn6],[btn7,btn8,btn9]]
    for x in range(3):
        if button[x][0]['text'] == button[x][1]['text'] and button[x][0]['text'] == button[x][2]['text'] and button[x][0]['text'] != '':
            messagebox.showinfo(message='Match found!')
            update()
    for x in range(3):
        if button[0][x]['text'] == button[1][x]['text'] and button[0][x]['text'] == button[2][x]['text'] and button[0][x]['text'] != '':
            messagebox.showinfo(message='Match found!')
            update()
    if button[0][0]['text'] == button[1][1]['text'] and button[0][0]['text'] == button[2][2]['text'] and button[0][0]['text'] != '':
        messagebox.showinfo(message='Match found!')
        update()
    if button[0][2]['text'] == button[1][1]['text'] and button[0][2]['text'] == button[2][0]['text'] and button[0][2]['text'] != '':
        messagebox.showinfo(message='Match found!')
        update()
#UI start here
root = Tk()
frame =Frame(root)
btn1 = Button(frame,text = value,fort=('normal',15),height=4,width = 8,command = lambda : func(btn1))
btn1 = Button(frame,text = value,fort=('normal',15),height=4,width = 8,command = lambda : func(btn1))
btn1 = Button(frame,text = value,fort=('normal',15),height=4,width = 8,command = lambda : func(btn1))
btn1 = Button(frame,text = value,fort=('normal',15),height=4,width = 8,command = lambda : func(btn1))
btn1 = Button(frame,text = value,fort=('normal',15),height=4,width = 8,command = lambda : func(btn1))
btn1 = Button(frame,text = value,fort=('normal',15),height=4,width = 8,command = lambda : func(btn1))

