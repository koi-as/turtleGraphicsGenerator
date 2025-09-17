import tkinter as tk
from tkinter import *
import turtle as turt
from turtle import *

win=tk.Tk()
win.geometry('400x400')
win.title('Draw Like A Turtle')
win.config(bg='light blue')

expl='''
    This is supposed to be a simple program that takes your input in the box below and draws an image in a new window. There are a few buttons below for you to use as you need. The first starts the drawing, and you can watch as the turtle draws you a masterpiece! The second gives you an additional entry field for you to add a new command to. The third just closes this window... Good luck!
    '''

command0=StringVar()

def draw():
    print('hello')

def newBox():
    print('oh no')
# title label for app
# explanation label
# button to initiate turtle program
# button to add function
# button to end program
# entry field to add function
# some kind of looping function that pushes a new entry field whenever a user asks for one
# I wonder what the limit could be?
Label(win, text='Draw Like A Turty!').place(x=150, y=0)
Label(win, text=expl, wraplength=window_width()).place(x=0, y=50)
Button(win, text='DRAW', command=draw, bg='light green').place(x=0, y=100)
Button(win, text='ADD BOX', command=newBox, bg='light blue').place(x=0, y=150)
Button(win, text='LEAVE', command=win.destroy, bg='red').place(x=0, y=200)
# Entry(win, textvariable=command0, relief=GROOFY)

# turt.mainloop()
win.mainloop()