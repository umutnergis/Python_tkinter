from tkinter import *

root = Tk()

myLabel = Label(root,text="Hello World",background="green")
myLabel1 = Label(root,text="Umut Nergis",background="red")
#myLabel.pack()
#Grid means place where you want to put your stuff
myLabel.grid(column=0,row=0)
myLabel1.grid(column=0,row=1)
#if you want you can put .grid() code after Label. It should work
root.mainloop()


