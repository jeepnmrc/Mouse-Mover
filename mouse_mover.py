#pip3 install pyautogui
#pip3 install keyboard
#pip3 install tkinter

from tkinter import *
import pyautogui

window = Tk()
window.title('Mouse Mover')
window.config(bg='cadetblue2')
Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.columnconfigure(window,0,weight=1)

status = BooleanVar()
status= True
def mouse_move():
    global status
    if status == True:
        pyautogui.moveRel(0,15)
        pyautogui.moveRel(0,-15)
        window.after(5000,mouse_move)
def mouse_mover_on():
    global status
    status = True
    mouse_move()
def mouse_mover_off():
    global status
    status = False

mouse_on = Button(window,text="Away",command=mouse_mover_on,width=50,height=2)
mouse_on.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)
mouse_off = Button(window,text='Back',command=mouse_mover_off,width=50,height=10)
mouse_off.grid(row=1,column=0,sticky=NSEW,padx=10,pady=10)

window.mainloop()
