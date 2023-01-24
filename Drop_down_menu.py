from tkinter import *

root = Tk()
root.title("Drop Down")
root.geometry("400x400")
def show():
    label = Label(root,text=click.get()).pack()

options = [
    "AUDI",
    "BMW",
    "RR",
    "MERCEDES"
]
click = StringVar()
click.set(options[0]) 
# You have to put * 
menu = OptionMenu(root,click,*options).pack()

myButton= Button(root,text="Clicked",command=show).pack()
root.mainloop()