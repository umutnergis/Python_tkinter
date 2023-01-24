from tkinter import *

root = Tk()
root.title("SLIDER")

root.geometry("400x400")

vertical = Scale(root,from_=0,to=500)
vertical.pack()

horizontal = Scale(root,from_=0,to=500,orient=HORIZONTAL)
horizontal.pack()



def click():
    my_vertical = Label(root,text= vertical.get()).pack()
    my_label = Label(root,text =horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

my_buton = Button(root,text="Click",command=click).pack()
root.mainloop()