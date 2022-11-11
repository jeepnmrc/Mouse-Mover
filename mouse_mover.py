#pip3 install pyautogui
#pip3 install keyboard
#pip3 install tkinter

from tkinter import *
import pyautogui
import keyboard
import time

window = Tk()
window.title('Mouse Mover')
window.config(bg='cadetblue2')
Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.columnconfigure(window,0,weight=1)

status = BooleanVar()
status= True
def mouse_mover_on():
    global status
    if status == True:
        pyautogui.moveRel(0,10)
        pyautogui.moveRel(0,-10)
        window.after(1000,mouse_mover_on)
def mouse_mover_off():
    global status
    status = False

mouse_on = Button(window,text="Away",command=mouse_mover_on,width=50,height=2)
mouse_on.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)
mouse_off = Button(window,text='Back',command=mouse_mover_off,width=50,height=10)
mouse_off.grid(row=1,column=0,sticky=NSEW,padx=10,pady=10)

window.mainloop()