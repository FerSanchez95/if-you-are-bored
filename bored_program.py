''' If you are bored you can use this program to found someting to do. https://www.boredapi.com/api/activity'''
from tkinter import *
from tkinter import ttk
import json
import requests

def do_request():
    '''Do the reques when the button is pressed.'''

def main():
    ''' X '''
    win = Tk()
    win.title("bored stuff")
    width = 300
    height = 200
    width_scr = win.winfo_screenwidth()
    height_scr = win.winfo_screenheight()
    x = (width_scr/2) - (width/2)
    y = (height_scr/2) - (height/2)
    win.geometry("%dx%d+%d+%d" % (width, height, x, y))

    sub_title = Label(win, text="Press to found somting to do", font=("bold", 10))
    sub_title.pack()
    btn = Button(win, text="botón")
    btn.pack()
    win.mainloop()

if __name__ == '__main__':
    main()
